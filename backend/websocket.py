from fastapi import WebSocket


# create socket manager that stores a list of websockets linked to channels
# each channel has a queue of messages to be sent to the channel
class SocketManager:
    def __init__(self) -> None:
        self.__sockets = []

    def register(self, websocket: WebSocket):
        self.__sockets.append(websocket)

    def unregister(self, websocket: WebSocket):
        self.__sockets.remove(websocket)

    async def broadcast(self, message: str):
        for socket in self.__sockets:
            await socket.send_json(message)


socket_manager = SocketManager()
