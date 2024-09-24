import secrets
from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

security = HTTPBasic()


def authenticate_username_and_password(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
) -> dict[str, str]:
    """ "Basic HTTP Authentication method function.

    Args:
        credentials (HTTPBasicCredentials): HTTP Basic Authentication credentials.

    Returns:
        str: The authenticated username.

    Raises:
        HTTPException: If the provided credentials are invalid.
    """
    # Validate username
    current_username_bytes = credentials.username.encode("utf8")
    correct_username_bytes = b"myself"
    is_correct_username = secrets.compare_digest(
        current_username_bytes, correct_username_bytes
    )

    # Validate password
    current_password_bytes = credentials.password.encode("utf8")
    correct_password_bytes = b"swordfish"
    is_correct_password = secrets.compare_digest(
        current_password_bytes, correct_password_bytes
    )

    if is_correct_username and is_correct_password:
        return credentials.username

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Basic"},
    )
