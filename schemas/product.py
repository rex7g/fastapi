def productEntity(item) -> dict:
    return {
        "id": (item["_id"]),
        "nombre": item["name"],
        "descripcion": item["descripcion"],
        "fechaEmision": item["fechaVencimiento"],
        "fechaVencimiento": item["fechaVencimiento"],
        "suplidor": item["suplidor"]
    }


def productsEntity(entity) -> list:
    return [productEntity(item) for item in entity]
