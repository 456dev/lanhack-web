from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse

import lanhackbackend.api.routes.ingest as ingest
from lanhackbackend.api.data.storage import storage

api_router = APIRouter()
api_router.include_router(ingest.ingest_router, prefix="/ingest")


# return all uids from server (get)
# json format: {
#   "uids": [
#       {"uid": "uid1", "timestamp": "ISO timestamp"}
#       {"uid": "uid2", "timestamp": "ISO timestamp"}
#   ],
# }
@api_router.get("/get-uids")
async def pull():
    uids = storage.get_uids()
    return JSONResponse(content={"status": "success", "uids": uids}, status_code=200)
