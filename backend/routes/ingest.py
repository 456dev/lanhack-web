from fastapi.responses import Response
from fastapi.routing import APIRouter

import backend.models.api as api_models
import backend.models.ingest as ingest_models
from backend.data.storage import storage
from backend.websocket import socket_manager

ingest_router = APIRouter()


@ingest_router.get("/status")
async def status() -> api_models.BaseStatusResponse:
    return api_models.SuccessfulResponse()


@ingest_router.post(
    "/push-uid",
    response_model=api_models.SuccessfulResponse,
    responses={400: {"model": api_models.ErroredResponse}},
)
async def push_uid(
    body: ingest_models.UIDModel, response: Response
) -> api_models.BaseStatusResponse:
    status, value = storage.push_uid(body.uid)
    if status:
        await socket_manager.broadcast(value)
        return api_models.SuccessfulResponse()
    else:
        response.status_code = 400
        return api_models.ErroredResponse(message=str(value))
