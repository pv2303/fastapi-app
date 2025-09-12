from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class ModelName(str, Enum):
    lm = "lm"
    plm = "plm"
    dl = "dl"


@app.get("/")
async def root():
    return {"message": "Hello World"}

# Usage of path parameters

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

# Rotas fixas tem que ser declaradas antes das rotas dinâmicas
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user_id(user_id: str):
    return {"user_id": user_id}

@app.get("/models/{model_name}")
async def read_model_name(model_name: ModelName):
    if model_name is ModelName.lm:
        return {"model_name": model_name, "message": "It is a linear regression"}
    elif model_name.value == "Panel Linear Regression":
        return {"model_name": model_name, "message": "It is a linear regression with panel data"}
    else:
        return{"model_name": model_name, "message": "It is a deep learning model. Fancy."}