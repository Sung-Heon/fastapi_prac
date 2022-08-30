# main.py
from fastapi import FastAPI

# fastapi는 starlette을 상속받음
##Starlette is a lightweight ASGI framework/toolkit, which is ideal for building async web services in Python.


app = FastAPI()


# Here the app variable will be an "instance" of the class FastAPI.
# This will be the main point of interaction to create all your API.

# A "path" is also commonly called an "endpoint" or a "route".
@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to your todo list."}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


# 이런식으로 뒤에 처리 가능
# 타입힌트 가능
# 만약 제3라이브로리 쓰고 await 기능제공안하면, asyncthdyddjqtdma.


from enum import Enum


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

#이런 식으로도 가능