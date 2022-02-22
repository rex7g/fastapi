
from fastapi import APIRouter,Response,status
from config.db import conn
from schemas.product import productsEntity, productEntity
from bson import ObjectId

from models.product import Product


productos=APIRouter()

@productos.get('/productos',tags=["products"])
def find_all_products():
    return productsEntity(conn.product.local.fin())





@productos.get('/productos/{id}',tags=["products"])
def find_products_byID(id:int):
    return productEntity(conn.local.product.find_oneproduct({"_id":ObjectId(id)}))



@productos.post('/productos',tags=["products"])
def create_products(product:Product):
    new_product=dict(product)
    del new_product["id"]
    id=conn.local.product.insert_one(new_product).inserted_id
    product=conn.local.user.find_one({"id":id})
    return productEntity







@productos.put('/productos{id}',tags=["products"])
def update_product():
    return "holamundo"

@productos.delete('/productos{id}',tags=["products"])
def delete_product():
    return "holamundo"