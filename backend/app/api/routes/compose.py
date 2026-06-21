"""Story composition endpoint — gather source material, get a Claude-written draft."""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Request

from app.models.compose import ComposeRequest, ComposeResponse
from app.services.composer import Composer, ComposerUnavailable

router = APIRouter(tags=["compose"])


def get_composer(request: Request) -> Composer:
    return request.app.state.composer


@router.get("/compose/status")
async def compose_status(composer: Composer = Depends(get_composer)) -> dict:
    return {"available": composer.available, "model": composer.settings.story_model}


@router.post("/compose", response_model=ComposeResponse)
async def compose(
    req: ComposeRequest, composer: Composer = Depends(get_composer)
) -> ComposeResponse:
    if not req.entities:
        raise HTTPException(status_code=400, detail="수집한 자료가 없습니다.")
    try:
        return await composer.compose(req)
    except ComposerUnavailable as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
