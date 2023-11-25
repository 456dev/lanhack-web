from fastapi import Router


router = Router()


# APP ROUTES
@router.get("/")
async def root():
    return {"result": 200}


# push uid to server (post)
@router.post("/push-uid/{uid}")
async def push(uid: str):
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
