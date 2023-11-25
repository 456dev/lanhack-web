from fastapi.responses import JSONResponse, Response
from fastapi.routing import APIRouter

import backend.models.api as api_models, backend.models.ingest as ingest_models
from backend.data.storage import storage

ingest_router = APIRouter()


@ingest_router.get("/status")
async def status() -> api_models.Status:
    return api_models.Success()


@ingest_router.post("/push-uid", response_model=api_models.Success, responses={400: {"model": api_models.Error}})
async def push_uid(body: ingest_models.UIDModel, response: Response) -> api_models.Status:
    result = storage.push_uid(body.uid)
    if result[0]:
        return api_models.Success()
    else:
        response.status_code = 400
        return api_models.Error(message=result[1])
