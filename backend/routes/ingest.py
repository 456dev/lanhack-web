from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from pydantic import BaseModel

from backend.data.storage import storage

ingest_router = APIRouter()


# check status of ingest (get)
@ingest_router.get("/status")
async def status():
    return JSONResponse(content={"status": "success"}, status_code=200)


# define model for push-uid (post)
class UIDModel(BaseModel):
    uid: str


# push uid to storage (post)
@ingest_router.post("/push-uid")
async def push_uid(body: UIDModel):
    if storage.push_uid(body.uid):
        return JSONResponse(content={"status": "success"}, status_code=200)
    else:
        return JSONResponse(content={"status": "error"}, status_code=500)
