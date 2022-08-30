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

from typing import Union



@app.get("/items/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: Union[int, None] = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item
#쿼리 파람. 몇개는 required 몇개는 required안되게 가능.

#
# get으로 바디에 넣는것은 굉장히 예외적인 상황에만 해야됨.
# To send data, you should use one of: POST (the more common), PUT, DELETE or PATCH.
#
# Sending a body with a GET request has an undefined behavior in the specifications, nevertheless, it is supported by FastAPI, only for very complex/extreme use cases.
#
# As it is discouraged, the interactive docs with Swagger UI won't show the documentation for the body when using GET, and proxies in the middle might not support it.

# 리퀘스트 바디를 선언하는 것은 pydantic으로 함.


from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


#None: 넣으면 optional임

@app.post("/items/")
async def create_item(item: Item):
    return item
