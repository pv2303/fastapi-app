from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel

from typing import Union

app = FastAPI()

class ModelName(str, Enum):
    lm = "lm"
    plm = "plm"
    dl = "dl"

# None indica que aquele atributo é opcional
class Product(BaseModel):
    id: int
    name: Union[str, None] = None
    price: float
    quantity: Union[int, None] = None

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
    

# O Pydantic define tipagem forte dos dados que você pode ter para uma certa estrutura de dados
# Com isso você pode criar produtos, sabendo exatamente os tipos importantes e opcionais para execução do programa
@app.post("/products/")
async def create_product(product: Product):
    return product