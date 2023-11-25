from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse

from backend.routes.ingest import ingest_router
from backend.data.storage import storage

api_router = APIRouter()

# link routes for ingest backend
api_router.include_router(ingest_router, prefix="/ingest")


# return all uids from storage (get)
# json format: {
#   "uids": [
#       {"uid": "uid1", "timestamp": "ISO timestamp"}
#       {"uid": "uid2", "timestamp": "ISO timestamp"}
#   ],
# }
@api_router.get("/get-uids")
async def get_uids():
    uids = storage.get_uids()
    return JSONResponse(content={"status": "success", "uids": uids}, status_code=200)
