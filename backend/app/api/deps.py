"""Shared FastAPI dependencies."""

from __future__ import annotations

from fastapi import Request

from app.connectors.manager import ConnectorManager


def get_manager(request: Request) -> ConnectorManager:
    """Return the process-wide ConnectorManager created during app startup."""
    return request.app.state.manager
