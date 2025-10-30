from fastapi import FastAPI
import uvicorn
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Producto(BaseModel):
    nombre: str
    precio: float
    en_stock: bool
    tags: Optional[list[str]] = None

# Definimos una ruta: cuando alguien vaya a la página principal ("/"), 
# le devolvemos un mensaje
@app.get("/")
def hola_mundo():
    return {"mensaje": "¡Hola, mundo!"}

@app.post("/producto/")
def crear_producto(producto: Producto):
    return {
        f"nombre": producto.nombre,
        f"precio": producto.precio,
        f"en_stock": producto.en_stock,
        f"tags": producto.tags
    }




# Ejecutar la aplicación
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
