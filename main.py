from fastapi import FastAPI
from routes.user import user
from routes.product import productos

app = FastAPI()

app.include_router(user)
app.include_router(productos)
