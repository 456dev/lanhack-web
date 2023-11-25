from fastapi import FastAPI
from routes import router
import uvicorn

# init fastapi
app = FastAPI()
app.include_router(router)

# run server
uvicorn.run(app, host="localhost", port=8000)
