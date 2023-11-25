from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from pydantic import BaseModel

from backend.data.storage import storage

ingest_router = APIRouter()


@ingest_router.get("/status")
async def root():
    return JSONResponse(content={"status": "success"}, status_code=200)


class UIDModel(BaseModel):
    uid: str


@ingest_router.post("/push-uid")
async def push(body: UIDModel):
    success = storage.push_uid(body.uid)
    if success:
        return JSONResponse(content={"status": "success"}, status_code=200)
    else:
        return JSONResponse(content={"status": "error"}, status_code=500)
