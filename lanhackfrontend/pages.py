from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi import APIRouter

pages_router = APIRouter()
templates = Jinja2Templates(directory="./lanhackfrontend")


@pages_router.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
