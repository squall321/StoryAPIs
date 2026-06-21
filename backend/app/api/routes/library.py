"""Browse the locally collected (ingested) library."""

from __future__ import annotations

import asyncio

from fastapi import APIRouter, Depends, Query, Request

from app.models.entities import StoryEntity
from app.store.repository import Repository

router = APIRouter(prefix="/library", tags=["library"])


def get_repo(request: Request) -> Repository:
    return request.app.state.repo


@router.get("/stats")
async def stats(repo: Repository = Depends(get_repo)) -> dict:
    return await asyncio.to_thread(repo.stats)


@router.get("/search")
async def search(
    q: str | None = None,
    source: str | None = None,
    type: str | None = None,
    limit: int = Query(50, ge=1, le=200),
    repo: Repository = Depends(get_repo),
) -> dict:
    items: list[StoryEntity] = await asyncio.to_thread(
        repo.search, q, source, type, limit
    )
    return {"count": len(items), "items": items}
