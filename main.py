from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import requests

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory = "templates")
redirStatusCodes = (301, 302)

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/")
async def check(request: Request, url: str = Form()):
    redirectedURL = requests.get(url)
    print(redirectedURL.status_code)
    return templates.TemplateResponse("checked.html", {"request": request, "redirURL": redirectedURL, "url": url})