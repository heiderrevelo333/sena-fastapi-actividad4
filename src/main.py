from fastapi import FastAPI
import uvicorn
from typing import Optional, List, Union
from pydantic import BaseModel

app = FastAPI()

class Producto(BaseModel):
    nombre: str
    precio: float
    en_stock: bool
    tags: Optional[list[str]] = None


class Orden(BaseModel):
    cliente: str
    items: List[str]


class Respuesta(BaseModel):
    valor: Union[str, int]

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


@app.get("/productos/buscar/")
def buscar_productos(nombre: str, categoria: Optional[str] = None):
    """Búsqueda por consulta. Devuelve los filtros recibidos."""
    return {"nombre": nombre, "categoria": categoria}


@app.post("/orden/")
def recibir_orden(orden: Orden):
    """Recibe una orden de compra y devuelve el número de items y el cliente."""
    return {"cliente": orden.cliente, "numero_items": len(orden.items)}


@app.post("/respuesta/")
def procesar_respuesta(respuesta: Respuesta):
    """Demuestra Union: devuelve el tipo detectado y el valor."""
    valor = respuesta.valor
    tipo = type(valor).__name__
    return {"tipo": tipo, "valor": valor}




# Ejecutar la aplicación
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
