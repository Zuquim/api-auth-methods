# api-auth-methods

Learning how different authentication methods work with FastAPI.

## Index

TODO

## HTTP basic authentication

### Overview

HTTP Basic Authentication is the most rudimentary authentication method available for APIs.
It involves sending the username and password in the `Authorization` header of the HTTP request.
The credentials are encoded using Base64, but they are not hashed or encrypted.
Unless used in conjunction with HTTPS, this is an insecure authentication mechanism.

### Example Flow

1. **Client Request**: The client sends a request with an `Authorization` header in the format `Basic <base64(username:password)>`.
2. **Server Verification**: The server decodes the credentials and verifies them.
3. **Access Granted/Denied**: Based on verification, the server either grants access or responds with an error.

```mermaid
sequenceDiagram
    participant Client
    participant Server

    Client->>Server: 1. Request with Authorization header (Basic <base64(username:password)>)
    Server->>Server: 2. Decode and verify credentials
    Server->>Client: 3. Response (200 OK or 401 Unauthorized)
