"""StoryAPIs FastAPI application entrypoint.

Run locally:
    cd backend
    pip install -r requirements.txt
    uvicorn app.main:app --reload
"""

from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import __version__
from app.api.routes import compose, health, search, sources
from app.config import get_settings
from app.connectors.manager import ConnectorManager
from app.services.composer import Composer


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()
    app.state.manager = ConnectorManager(settings)
    app.state.composer = Composer(settings)
    try:
        yield
    finally:
        await app.state.manager.aclose()


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(
        title="StoryAPIs",
        version=__version__,
        description=(
            "A unified gateway to world knowledge, history, mythology and "
            "literature — source material for creative writing."
        ),
        lifespan=lifespan,
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(health.router, prefix="/api")
    app.include_router(sources.router, prefix="/api")
    app.include_router(search.router, prefix="/api")
    app.include_router(compose.router, prefix="/api")

    @app.get("/")
    async def root() -> dict:
        return {
            "name": "StoryAPIs",
            "version": __version__,
            "docs": "/docs",
            "endpoints": ["/api/health", "/api/sources", "/api/search?q=..."],
        }

    return app


app = create_app()
