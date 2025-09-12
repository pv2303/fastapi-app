'''
Script apenas para requests testes do main.py
'''
from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_new_prod(new_product_data: dict):
    response = client.post(
        "/products/",
        
        
    )