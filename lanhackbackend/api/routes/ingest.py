from fastapi.requests import Request
from fastapi.responses import Response, JSONResponse
from fastapi.routing import APIRouter

from lanhackbackend.api.data.storage import storage

ingest_router = APIRouter()


@ingest_router.get("/status")
async def root():
    response = JSONResponse({"status": "success"})
    response.status_code = 200
    return response


@ingest_router.post("/cardread")
async def push(request: Request):
    # todo: use models
    json = await request.json()
    success = storage.push_uid(json["uid"])
    return Response(status_code=200 if success else 400)
