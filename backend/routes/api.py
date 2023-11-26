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
    except RuntimeError:
        socket_manager.unregister(websocket)
