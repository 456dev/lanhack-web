from fastapi.routing import APIRouter
from fastapi.requests import Request


router = APIRouter()


# APP ROUTES
@router.get("/")
async def root():
    return {"result": 200}


# push uid to server (post)
# uid is in json format in body
# return 200 if in format: {"uid": "uid1"}
@router.post("/push-uid")
async def push(request: Request):
    json = await request.json()
    print(json)
    return {"result": 200}


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
    return {"result": 200}
