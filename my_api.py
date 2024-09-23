from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles 
from fastapi.templating import Jinja2Templates
from enum import Enum
from pathlib import Path
import json
from config import Config

files_path = Config.files_path
my_file = files_path.joinpath("temp.json")


app = FastAPI(host='0,0,0,0',port=8000)

app.mount("/static",
          StaticFiles(directory="static"),
          name="static"
          )

templates = Jinja2Templates(directory="templates")

class Informations(str , Enum):
    capteur = "capteur"

@app.get("/")
async def api_root(request: Request):
    with open(my_file,"r") as temp_val:
        temp = json.load(temp_val)
    
    return templates.TemplateResponse("raspberry.html",
                                      {"request": request,
                                       "temp":temp
                                       } )
@app.get("/api/info")
async def get_info():
    return {"name": "mon mac"}

