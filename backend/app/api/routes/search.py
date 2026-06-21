"""Federated search across all (or selected) connectors, plus single-record fetch."""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query

from app.api.deps import get_manager
from app.connectors.manager import ConnectorManager
from app.models.entities import SearchResponse, StoryEntity

router = APIRouter(tags=["search"])

# Cap full-text payloads so a multi-megabyte book doesn't blow up the response.
_FULLTEXT_CAP = 200_000


@router.get("/search", response_model=SearchResponse)
async def search(
    q: str = Query(..., min_length=1, description="search query"),
    sources: str | None = Query(
        None, description="comma-separated connector ids; default = all"
    ),
    limit: int = Query(10, ge=1, le=50),
    manager: ConnectorManager = Depends(get_manager),
) -> SearchResponse:
    source_ids = (
        [s.strip() for s in sources.split(",") if s.strip()] if sources else None
    )
    return await manager.search(q, source_ids=source_ids, limit=limit)


@router.get("/fulltext")
async def fulltext(
    id: str = Query(..., description='entity id, e.g. "gutendex:1342"'),
    manager: ConnectorManager = Depends(get_manager),
) -> dict:
    text = await manager.fulltext(id)
    if text is None:
        raise HTTPException(status_code=404, detail="no full text for this item")
    length = len(text)
    truncated = length > _FULLTEXT_CAP
    return {
        "id": id,
        "text": text[:_FULLTEXT_CAP],
        "length": length,
        "truncated": truncated,
    }


@router.get("/sources/{source_id}/items/{record_id:path}", response_model=StoryEntity)
async def fetch_item(
    source_id: str,
    record_id: str,
    manager: ConnectorManager = Depends(get_manager),
) -> StoryEntity:
    connector = manager.get(source_id)
    if connector is None:
        raise HTTPException(status_code=404, detail=f"unknown source: {source_id}")
    entity = await connector.fetch(record_id)
    if entity is None:
        raise HTTPException(status_code=404, detail="record not found")
    return entity
