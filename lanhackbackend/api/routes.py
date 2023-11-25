from fastapi.routing import APIRouter
from fastapi.requests import Request
from fastapi.responses import Response

from lanhackbackend.api.data.storage import storage

router = APIRouter()


# APP ROUTES
@router.get("/")
async def root():
    return Response(status_code=200)


# push uid to server (post)
# uid is in json format in body
# return 200 if in format: {"uid": "uid1"}
@router.post("/ingest/cardread")
async def push(request: Request):
    json = await request.json()
    success = storage.push_uid(json["uid"])
    return Response(status_code=200 if success else 500)


# return all uids from server (get)
# format: {
#   "uids": [
#       {"uid": "uid1", "timestamp": "25-11-23 00:00:00"}
#       {"uid": "uid2", "timestamp": "25-11-23 00:00:00"}
#   ],
#   "result": 200
# }
@router.get("/get-uids")
async def pull():
    return storage.get_uids()
