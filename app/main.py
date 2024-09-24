from typing import Annotated

from fastapi import Depends, FastAPI, status

from app.api_key_auth import authenticate_api_key
from app.http_basic_auth import authenticate_username_and_password
from app.schemas.response.health import HealthCheckResponse

app = FastAPI()


@app.get("/")
async def root():
    """Dummy root endpoint."""
    return {"message": "Hello World"}


@app.get("/health", response_model=HealthCheckResponse, status_code=status.HTTP_200_OK)
async def health():
    """Health check endpoint."""
    return HealthCheckResponse(message="OK")


@app.get("/auth-methods/http-basic-authentication")
def http_basic_authentication(
    username: Annotated[str, Depends(authenticate_username_and_password)]
):
    """HTTP Basic Authentication method endpoint.

    Args:
        username (str): The authenticated username.

    Returns:
        dict: A message indicating the authenticated username.
    """
    return {"message": f"Authenticated as {username}"}


@app.get("/auth-methods/api-key-authentication")
def api_key_authentication(api_key: Annotated[bool, Depends(authenticate_api_key)]):
    """API Key Authentication method endpoint.

    Args:
        api_key (bool): Whether the API key is valid or not.

    Returns:
        dict: A message indicating the authentication status.
    """
    return {"message": "API Key authenticated"}
