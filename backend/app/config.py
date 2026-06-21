"""Application settings, loaded from environment / `.env` (prefix: STORYAPIS_)."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

# backend/ directory — anchors data paths so they're CWD-independent.
_BACKEND_DIR = Path(__file__).resolve().parents[1]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="STORYAPIS_",
        extra="ignore",
        case_sensitive=False,
    )

    # --- App ---
    app_name: str = "StoryAPIs"
    environment: str = "development"
    http_timeout: float = 20.0
    user_agent: str = (
        "StoryAPIs/0.1 (+https://github.com/squall321/StoryAPIs) "
        "knowledge-aggregator for creative writing"
    )
    cors_origins: list[str] = ["http://localhost:5173", "http://127.0.0.1:5173"]

    # --- Local collected library (ingested data) ---
    library_db_path: str = str(_BACKEND_DIR / "data" / "library.db")

    # --- Optional connector credentials ---
    europeana_api_key: str | None = None
    geonames_username: str | None = None
    smithsonian_api_key: str | None = None
    ctext_api_key: str | None = None
    trove_api_key: str | None = None
    data_go_kr_key: str | None = None

    # --- Story generation (Claude) ---
    anthropic_api_key: str | None = None
    story_model: str = "claude-opus-4-8"

    @field_validator("cors_origins", mode="before")
    @classmethod
    def _split_origins(cls, v: object) -> object:
        if isinstance(v, str):
            return [o.strip() for o in v.split(",") if o.strip()]
        return v


@lru_cache
def get_settings() -> Settings:
    return Settings()
