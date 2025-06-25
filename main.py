from typing import Union
from fastapi import FastAPI, APIRouter
import mouse
import json

app = FastAPI()
router = APIRouter()

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

app.include_router(router)



