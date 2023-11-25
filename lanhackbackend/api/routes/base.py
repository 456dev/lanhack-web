from fastapi.routing import APIRouter

import lanhackbackend.api.routes.ingest as ingest
from lanhackbackend.api.data.storage import storage

api_router = APIRouter()

api_router.include_router(ingest.ingest_router, prefix="/ingest")


# return all uids from server (get)
# format: {
#   "uids": [
#       {"uid": "uid1", "timestamp": "25-11-23 00:00:00"}
#       {"uid": "uid2", "timestamp": "25-11-23 00:00:00"}
#   ],
#   "result": 200
# }
@api_router.get("/get-uids")
async def pull():
    return storage.get_uids()
