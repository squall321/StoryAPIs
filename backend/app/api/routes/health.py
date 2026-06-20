"""Health & metadata endpoints."""

from __future__ import annotations

from fastapi import APIRouter, Depends

from app import __version__
from app.api.deps import get_manager
from app.connectors.manager import ConnectorManager

router = APIRouter(tags=["meta"])


@router.get("/health")
async def health(manager: ConnectorManager = Depends(get_manager)) -> dict:
    return {
        "status": "ok",
        "version": __version__,
        "connectors": len(manager.connectors),
    }
