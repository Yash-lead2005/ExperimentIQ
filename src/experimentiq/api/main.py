"""FastAPI application entry point."""

from fastapi import FastAPI
from pydantic import BaseModel

from experimentiq import __version__

app = FastAPI(
    title="ExperimentIQ API",
    description="Backend for A/B test analysis, diagnostics, CUPED, ML and uplift.",
    version=__version__,
)


class HealthResponse(BaseModel):
    """Response schema for the health-check endpoint."""

    status: str
    service: str
    version: str


@app.get("/health", response_model=HealthResponse, tags=["system"])
def health() -> HealthResponse:
    """Return a simple status payload so clients can confirm the API is up."""
    return HealthResponse(status="ok", service="experimentiq-api", version=__version__)