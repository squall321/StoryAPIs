"""Request/response models for the Claude story composer (/api/compose)."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field

from app.models.entities import StoryEntity


class ComposeOptions(BaseModel):
    genre: str | None = None
    length: Literal["short", "medium", "long"] = "medium"
    language: Literal["ko", "en"] = "ko"
    tone: str | None = None


class ComposeRequest(BaseModel):
    brief: str = Field(..., min_length=1, description="what the writer wants")
    entities: list[StoryEntity] = Field(default_factory=list)
    # ids resolved from the local library (collected corpus) and merged in
    entity_ids: list[str] = Field(default_factory=list)
    options: ComposeOptions = Field(default_factory=ComposeOptions)


class UsedSource(BaseModel):
    id: str
    title: str
    source_name: str
    source_url: str | None = None


class ComposeResponse(BaseModel):
    draft: str
    model: str
    language: str
    used_sources: list[UsedSource] = Field(default_factory=list)
    usage: dict | None = None
