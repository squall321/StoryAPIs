"""The unified knowledge model.

Every connector — whether it speaks to 조선왕조실록, Wikidata, The Met, or a
folktale index — normalizes its records into a single :class:`StoryEntity`
shape so the frontend, search, and (later) the story-composer can treat all of
world knowledge uniformly.
"""

from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum

from pydantic import BaseModel, Field


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


class EntityType(str, Enum):
    """Coarse classification shared across every source."""

    PERSON = "person"
    PLACE = "place"
    EVENT = "event"
    PERIOD = "period"
    WORK = "work"  # book, poem, play, scripture, artwork
    DEITY = "deity"
    CREATURE = "creature"  # monsters, mythical beasts, yokai...
    ARTIFACT = "artifact"  # objects, weapons, relics
    ORGANIZATION = "organization"
    CONCEPT = "concept"
    MOTIF = "motif"  # narrative motif / folktale type
    OTHER = "other"


class License(BaseModel):
    """Rights summary — critical for deciding what may be reused in a new story."""

    name: str = "unknown"
    url: str | None = None
    commercial_ok: bool | None = None
    attribution_required: bool | None = None


class Provenance(BaseModel):
    """Where a record came from. Always present so nothing is unattributable."""

    source_id: str
    source_name: str
    source_record_id: str | None = None
    source_url: str | None = None
    license: License = Field(default_factory=License)
    language: str | None = None
    retrieved_at: datetime = Field(default_factory=_utcnow)


class TimeRef(BaseModel):
    """A fuzzy time anchor. Negative years denote BCE."""

    label: str | None = None
    start_year: int | None = None
    end_year: int | None = None


class GeoRef(BaseModel):
    label: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    country: str | None = None


class MediaRef(BaseModel):
    type: str = "image"  # image | audio | video | iiif
    url: str
    thumbnail_url: str | None = None
    caption: str | None = None
    license: License | None = None


class Relation(BaseModel):
    """A typed edge to another entity (e.g. ``child_of``, ``occurred_during``)."""

    predicate: str
    target_label: str | None = None
    target_id: str | None = None
    target_source: str | None = None


class StoryEntity(BaseModel):
    """A single normalized knowledge node — the atom of the whole platform."""

    id: str  # globally unique, conventionally "{source_id}:{record_id}"
    type: EntityType = EntityType.OTHER
    title: str
    aliases: list[str] = Field(default_factory=list)
    summary: str | None = None
    description: str | None = None
    full_text: str | None = None  # populated only for full-text works on demand
    languages: list[str] = Field(default_factory=list)
    tags: list[str] = Field(default_factory=list)
    time: TimeRef | None = None
    places: list[GeoRef] = Field(default_factory=list)
    media: list[MediaRef] = Field(default_factory=list)
    relations: list[Relation] = Field(default_factory=list)
    provenance: Provenance
    extra: dict = Field(default_factory=dict)


class SearchHit(BaseModel):
    entity: StoryEntity
    score: float | None = None
    snippet: str | None = None


class SourceResult(BaseModel):
    """Per-connector slice of a federated search."""

    source_id: str
    source_name: str
    hits: list[SearchHit] = Field(default_factory=list)
    total: int | None = None
    error: str | None = None
    elapsed_ms: int | None = None


class SearchResponse(BaseModel):
    query: str
    results: list[SourceResult] = Field(default_factory=list)
    total_hits: int = 0
    elapsed_ms: int | None = None
