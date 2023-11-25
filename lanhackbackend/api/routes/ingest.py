from fastapi.requests import Request
from fastapi.responses import Response
from fastapi.routing import APIRouter

from lanhackbackend.api.data.storage import storage

ingest_router = APIRouter()


@ingest_router.get("/status")
async def root():
    return Response(status_code=200)


@ingest_router.post("/cardread")
async def push(request: Request):
    # todo: use models
    json = await request.json()
    success = storage.push_uid(json["uid"])
    return Response(status_code=200 if success else 400)
