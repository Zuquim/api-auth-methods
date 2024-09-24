from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader

API_KEY = "my-secret-api-key"
API_KEY_NAME = "X-API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME)


def authenticate_api_key(api_key: str = Depends(api_key_header)):
    """API Key Authentication method function.

    Args:
        api_key: The API Key provided by the client.

    Returns:
        True if the API Key is valid, otherwise raises an HTTPException.

    Raises:
        HTTPException: If the API Key is invalid.
    """
    if api_key == API_KEY:
        return True
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid API Key",
        headers={"WWW-Authenticate": "Bearer"},
    )
