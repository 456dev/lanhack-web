from fastapi.templating import Jinja2Templates
from fastapi import Request
from lanhackbackend.main import app

pages_router = app
templates = Jinja2Templates(directory="lanhackfrontend/templates")


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
