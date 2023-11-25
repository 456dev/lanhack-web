from fastapi import FastAPI
from api.routes import router
import uvicorn

from api.data.storage import storage

# init fastapi
app = FastAPI()
app.include_router(router, prefix="/api")

# init storage
storage.init()

# run server
uvicorn.run(app, host="localhost", port=8000)
