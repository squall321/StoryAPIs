"""Ingestion: pull from live connectors and store into the local library."""

from app.ingest.pipeline import IngestPipeline

__all__ = ["IngestPipeline"]
