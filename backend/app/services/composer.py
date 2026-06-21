"""Story composer — turns collected source material into a new story draft via Claude.

The whole point of StoryAPIs: take the `StoryEntity` records a writer has gathered
and have Claude weave them into an original story/outline, grounded in (and citing)
the real sources.
"""

from __future__ import annotations

from app.config import Settings
from app.models.compose import ComposeRequest, ComposeResponse, UsedSource
from app.models.entities import StoryEntity

# Output ceilings per requested length (kept < 16k so non-streaming stays safe).
_LENGTH_TOKENS = {"short": 1500, "medium": 4500, "long": 12000}
_FULLTEXT_EXCERPT = 800


class ComposerUnavailable(RuntimeError):
    """Raised when no Anthropic API key is configured."""


class Composer:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self._client = None
        if settings.anthropic_api_key:
            # Imported lazily so the backend runs without the key for everything else.
            from anthropic import AsyncAnthropic

            self._client = AsyncAnthropic(api_key=settings.anthropic_api_key)

    @property
    def available(self) -> bool:
        return self._client is not None

    async def compose(self, req: ComposeRequest) -> ComposeResponse:
        if self._client is None:
            raise ComposerUnavailable(
                "Anthropic API 키가 설정되지 않았습니다. backend/.env 에 "
                "STORYAPIS_ANTHROPIC_API_KEY 를 설정하세요."
            )

        lang = req.options.language
        system = _system_prompt(lang)
        user = _user_prompt(req)
        max_tokens = _LENGTH_TOKENS[req.options.length]

        message = await self._client.messages.create(
            model=self.settings.story_model,
            max_tokens=max_tokens,
            system=system,
            messages=[{"role": "user", "content": user}],
        )
        draft = "".join(b.text for b in message.content if b.type == "text").strip()

        return ComposeResponse(
            draft=draft,
            model=message.model,
            language=lang,
            used_sources=[_to_source(e) for e in req.entities],
            usage={
                "input_tokens": message.usage.input_tokens,
                "output_tokens": message.usage.output_tokens,
            },
        )


def _system_prompt(lang: str) -> str:
    if lang == "en":
        return (
            "You are a master storyteller and worldbuilder helping a writer craft a new, "
            "original work. You are given source material the writer has gathered from real "
            "historical, mythological, and literary databases. Ground the story in this "
            "material: weave in its motifs, characters, places, events, and atmosphere, and "
            "stay faithful to real history where it appears. Do not copy long passages "
            "verbatim — synthesize. Cite the sources you draw on by their title. "
            "Respond in English, in Markdown: a title, the story or outline, then a short "
            "'## Sources' list of the titles you used. Be vivid and specific."
        )
    return (
        "당신은 작가가 새로운 창작물을 쓰도록 돕는 뛰어난 이야기꾼이자 세계관 설계자입니다. "
        "작가가 실제 역사·신화·문학 데이터베이스에서 모아온 원천 자료가 주어집니다. "
        "그 자료에 뿌리내려 이야기를 지으세요: 모티프·인물·장소·사건·분위기를 엮되, 실제 "
        "역사가 등장하면 그 사실에 충실하세요. 긴 원문을 그대로 베끼지 말고 재창조하세요. "
        "참고한 자료는 제목으로 인용하세요. 한국어로, 마크다운 형식으로 답하세요: 제목, "
        "이야기 또는 개요, 그리고 마지막에 사용한 자료 제목들을 '## 출처' 목록으로 정리하세요. "
        "생생하고 구체적으로 쓰세요."
    )


def _user_prompt(req: ComposeRequest) -> str:
    opt = req.options
    lines: list[str] = []
    head = "Brief" if opt.language == "en" else "작가의 요청"
    lines.append(f"# {head}\n{req.brief}\n")

    meta: list[str] = []
    if opt.genre:
        meta.append(f"genre/장르: {opt.genre}")
    if opt.tone:
        meta.append(f"tone/톤: {opt.tone}")
    length_label = {"short": "짧게", "medium": "보통", "long": "길게"}[opt.length]
    meta.append(f"length/분량: {opt.length} ({length_label})")
    if meta:
        lines.append("(" + " · ".join(meta) + ")\n")

    src_head = "Source material" if opt.language == "en" else "원천 자료"
    lines.append(f"# {src_head} ({len(req.entities)})\n")
    for i, e in enumerate(req.entities, 1):
        lines.append(_format_entity(i, e))

    return "\n".join(lines)


def _format_entity(idx: int, e: StoryEntity) -> str:
    parts = [f"## {idx}. {e.title}  · [{e.type.value}] · {e.provenance.source_name}"]
    if e.summary:
        parts.append(e.summary)
    if e.description and e.description != e.summary:
        parts.append(e.description)
    if e.time and e.time.label:
        parts.append(f"- 시대/time: {e.time.label}")
    places = [p.label or p.country for p in e.places if (p.label or p.country)]
    if places:
        parts.append(f"- 장소/place: {', '.join(places)}")
    if e.tags:
        parts.append(f"- 태그/tags: {', '.join(e.tags[:10])}")
    if e.full_text:
        excerpt = e.full_text[:_FULLTEXT_EXCERPT]
        suffix = "…" if len(e.full_text) > _FULLTEXT_EXCERPT else ""
        parts.append(f"- 원문 발췌/excerpt: {excerpt}{suffix}")
    if e.provenance.source_url:
        parts.append(f"- 출처/source: {e.provenance.source_url}")
    return "\n".join(parts) + "\n"


def _to_source(e: StoryEntity) -> UsedSource:
    return UsedSource(
        id=e.id,
        title=e.title,
        source_name=e.provenance.source_name,
        source_url=e.provenance.source_url,
    )
