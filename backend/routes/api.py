from fastapi.routing import APIRouter, WebSocket
from fastapi.responses import JSONResponse
from fastapi import WebSocketDisconnect

from backend.routes.ingest import ingest_router
import backend.models.api as api_models

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
@api_router.get("/get-uids", response_model=api_models.UidGetResponse)
async def get_uids():
    return api_models.UidGetResponse(uids=storage.get_uids())


@api_router.post("/clear-uids")
async def clear_uids() -> api_models.BaseStatusResponse:
    storage.clear_uids()
    return api_models.SuccessfulResponse()


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
    except WebSocketDisconnect:
        socket_manager.unregister(websocket)
