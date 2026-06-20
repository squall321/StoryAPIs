"""Connector framework: a common contract every data source implements.

A connector translates one external knowledge source into the unified
:class:`~app.models.entities.StoryEntity` model. Connectors register themselves
with the global registry via the :func:`register` decorator; the
:class:`~app.connectors.manager.ConnectorManager` then instantiates and
orchestrates them.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from enum import Enum

import httpx
from pydantic import BaseModel, Field

from app.config import Settings
from app.models.entities import EntityType, License, SearchHit, StoryEntity


class Capability(str, Enum):
    SEARCH = "search"  # keyword search -> list of entities
    FETCH = "fetch"  # fetch one entity by id
    FULLTEXT = "fulltext"  # can return the full source text of a work
    LIST = "list"  # can enumerate / browse without a query


class ConnectorMeta(BaseModel):
    """Self-description shown in the source catalog and the UI."""

    id: str
    name: str
    description: str
    homepage: str | None = None
    regions: list[str] = Field(default_factory=list)
    languages: list[str] = Field(default_factory=list)
    entity_types: list[EntityType] = Field(default_factory=list)
    capabilities: list[Capability] = Field(default_factory=list)
    license: License = Field(default_factory=License)
    auth_required: bool = False
    enabled: bool = True
    notes: str | None = None


class BaseConnector(ABC):
    """Base class for all connectors.

    Subclasses set a class-level :attr:`meta` and implement :meth:`search`.
    They receive a shared async HTTP client and the app settings so credentials
    and a polite ``User-Agent`` are handled centrally.
    """

    meta: ConnectorMeta

    def __init__(self, client: httpx.AsyncClient, settings: Settings) -> None:
        self.client = client
        self.settings = settings

    @abstractmethod
    async def search(self, query: str, *, limit: int = 10) -> list[SearchHit]:
        """Return up to ``limit`` normalized hits for ``query``."""

    async def fetch(self, record_id: str) -> StoryEntity | None:
        """Fetch a single full record by its source record id. Optional."""
        return None

    async def health(self) -> bool:
        """Cheap liveness probe; override for a lighter check than a search."""
        try:
            await self.search("test", limit=1)
            return True
        except Exception:
            return False

    # --- helpers for subclasses ---
    def make_id(self, record_id: str | int) -> str:
        return f"{self.meta.id}:{record_id}"

    def available(self) -> bool:
        """Whether this connector has whatever credentials it needs to run."""
        return True


# --- global registry -------------------------------------------------------

_REGISTRY: dict[str, type[BaseConnector]] = {}


def register(cls: type[BaseConnector]) -> type[BaseConnector]:
    """Class decorator that adds a connector to the global registry."""
    if not getattr(cls, "meta", None):
        raise TypeError(f"{cls.__name__} must define a class-level `meta`")
    if cls.meta.id in _REGISTRY:
        raise ValueError(f"duplicate connector id: {cls.meta.id!r}")
    _REGISTRY[cls.meta.id] = cls
    return cls


def all_connector_classes() -> list[type[BaseConnector]]:
    return list(_REGISTRY.values())
