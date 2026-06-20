"""Connector package.

Importing this package imports every connector module, which triggers their
``@register`` decorators so the registry is fully populated.
"""

from app.connectors import (  # noqa: F401  (imported for side-effect: registration)
    gutendex,
    met,
    openlibrary,
    poetrydb,
    wikidata,
)
from app.connectors.base import (
    BaseConnector,
    Capability,
    ConnectorMeta,
    all_connector_classes,
    register,
)

__all__ = [
    "BaseConnector",
    "Capability",
    "ConnectorMeta",
    "all_connector_classes",
    "register",
]
