from fastapi import FastAPI, status

from schemas.response.health import HealthCheckResponse

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health", response_model=HealthCheckResponse, status_code=status.HTTP_200_OK)
async def health():
    return HealthCheckResponse(message="OK")
