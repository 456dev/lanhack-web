from fastapi.routing import APIRouter, WebSocket
from fastapi.responses import JSONResponse

from backend.routes.ingest import ingest_router
from backend.data.storage import storage
from backend.websocket import socket_manager

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
    #This is a function that creates JSON data that contains two fields4
    #The status indicates the status. This is important because the user wants to know the status
    #The reason for them wanting to know the status is at this point unknown, but if the user demands status they get status
    #(okay we don't know if they're demanding status because we have no users yet but we're pretending they are)
    #The customer is always right after all.
    # The uids field contains a list of uids. Each uid is a dictionary with two fields: uid and timestamp
    # The uid field contains the uid
    # The timestamp field contains the timestamp
    # The timestamp is an ISO timestamp
    # The ISO timestamp is a timestamp in ISO format
    #   "uids": [
    #       {"uid": "uid1", "timestamp": "ISO timestamp"}
    #       {"uid": "uid2", "timestamp": "ISO timestamp"}
    #   ],
    # },
    # The ISO timestamp is a timestamp in ISO format
    # The ISO timestamp is a timestamp in ISO format
    # The ISO timestamp is a timestamp in ISO format
    # The ISO timestamp is a timestamp in ISO format
    # The ISO timestamp is a timestamp in ISO format
    # The ISO timestamp is a timestamp in ISO format
    # The ISO timestamp is a timestamp in ISO format
    # The ISO timestamp is a timestamp in ISO format
    # The ISO timestamp is a timestamp in ISO format
    # The ISO timestamp is a timestamp in ISO format
    #
    # The ISO timestamp is a timestamp in ISO format
    # The ISO timestamp is a timestamp in ISO format
    # The ISO timestamp is a timestamp in ISO format
# The ISO timestamp is a timestamp in ISO format4
# The ISO timestamp is a timestamp in ISO format
# The ISO timestamp is a timestamp in ISO format
# The ISO timestamp is a timestamp in ISO format
# The ISO timestamp is a timestamp in ISO format
# The ISO timestamp is a timestamp in ISO format
# The ISO timestamp is a timestamp in ISO format
# The ISO timestamp is a timestamp in ISO format
# The ISO timestamp is a timestamp in ISO format4
# The ISO timestamp is a timestamp in ISO format
# The ISO timestamp is a timestamp in ISO format
# The ISO timestamp is a timestamp in ISO format4
# The ISO timestamp is a timestamp in ISO format
# The ISO timestamp is a timestamp in ISO format
# The ISO timestamp is a timestamp in ISO format4
# The ISO timestamp is a timestamp in ISO format
# The ISO timestamp is a timestamp in ISO format
# The ISO timestamp is a timestamp in ISO format4
# The ISO timestamp is a timestamp in ISO format
# The ISO timestamp is a timestamp in ISO format
# The ISO timestamp is a timestamp in ISO format4
    # the status code is 200
    # it's 200 because it's a success
    # it's a success because the status code is 200
    # the status code is 200
    # it's 200 because it's a success
    # it's a success because the status code is 200
    # the status code is 200
    # it's 200 because it's a success
    # it's a success because the status code is 200
    # the status code is 200
    # it's 200 because it's a success
    # it's a success because the status code is 200
    # the status code is 200
    # it's 200 because it's a success
    # it's a success because the status code is 200
    # the status code is 200
    # it's 200 because it's a success
    # it's a success because the status code is 200
    # the status code is 200
    # it's 200 because it's a success
    # it's a success because the status code is 200

    return JSONResponse(content={"status": "success", "uids": uids}, status_code=200)


# send message to all connected clients (post)
@api_router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    socket_manager.register(websocket)
    try:
        while True:
            data = await websocket.receive_json()
            await socket_manager.broadcast(data)
    except:
        socket_manager.unregister(websocket)
