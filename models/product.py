from typing import Optional
from pydantic import BaseModel

class Product(BaseModel):
    id: int
    nombre: str
    descripcion: str
    fechaEmision: str
    fechaVencimiento:str
    suplidor:Optional[str]
    lote:str
