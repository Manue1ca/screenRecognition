from typing import Union
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
import json
import pyautogui

app = FastAPI()
router = APIRouter()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def read_root():
    return 'Hello World!'

@app.get('/checkPosition')
def checkPosition():
    with open('conf.json', 'r') as file:
        data = json.load(file)
    return {f"Положение рамки захвата: {data['LU']}"}

@router.post('/changePosition/')
def changePosition(a:int,b:int,pos:str):
    confPos = {
        "LU":[a,b,pos]
    }
    with open('conf.json', 'w') as json_file:
        json.dump(confPos, json_file)
    return 'Позиция изменена и внесена в файл конфигурации'

@router.get('/getPosition')
def changePosition():
    currentMouseX, currentMouseY = pyautogui.position()
    # return f'X={currentMouseX} Y={currentMouseY}'
    return {
        'x':currentMouseX,
        'y':currentMouseY
    }


app.include_router(router)



