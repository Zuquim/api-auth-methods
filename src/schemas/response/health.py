from pydantic import BaseModel


class HealthCheckResponse(BaseModel):
    """Health check response schema."""

    message: str
