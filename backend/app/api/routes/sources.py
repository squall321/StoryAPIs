"""Catalog of available data sources (connectors)."""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException

from app.api.deps import get_manager
from app.connectors.manager import ConnectorManager

router = APIRouter(prefix="/sources", tags=["sources"])


@router.get("")
async def list_sources(manager: ConnectorManager = Depends(get_manager)) -> dict:
    metas = manager.list_meta()
    return {"count": len(metas), "sources": metas}


@router.get("/{source_id}/health")
async def source_health(
    source_id: str, manager: ConnectorManager = Depends(get_manager)
) -> dict:
    connector = manager.get(source_id)
    if connector is None:
        raise HTTPException(status_code=404, detail=f"unknown source: {source_id}")
    ok = await connector.health()
    return {"source_id": source_id, "healthy": ok}
