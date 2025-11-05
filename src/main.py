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
    

class Perfil(BaseModel):
    usuario: str
    bio: Optional[str] = None
    intereses: Optional[List[str]] = None
    
class Calificacion(BaseModel):
    curso: str
    nota: float 
    
class Config(BaseModel):
    modo: str = "produccion"
    version: float = 1.0

class Estricto(BaseModel):
    cantidad: int
    


# Definimos una ruta: cuando alguien vaya a la página principal ("/"), 
# le devolvemos un mensaje
@app.get("/")
def saludo():
    return {"mensaje": "¡Bienvenido a nuestro test_project!"}

@app.post("/producto/")
def crear_producto(producto: Producto):
    return {
        "nombre": producto.nombre,
        "precio": producto.precio,
        "en_stock": producto.en_stock,
        "tags": producto.tags
    }


@app.get("/producto/buscar/")
def buscar_producto(nombre: str, categoria: Optional[str] = None):
    """Búsqueda por consulta. Devuelve los filtros recibidos."""
    return {"nombre": nombre, "categoria": categoria}


@app.post("/orden/")
def recibir_orden(orden: Orden):
    """Recibe una orden de compra y devuelve el número de items y el cliente."""
    return {"cliente": orden.cliente, "total_items": len(orden.items)}


@app.post("/respuesta/")
def procesar_respuesta(respuesta: Respuesta):
    """Demuestra Union: devuelve el tipo detectado y el valor."""
    valor = respuesta.valor
    tipo = type(valor).__name__
    return {"tipo": tipo, "valor": valor}

@app.post("/perfil/")
def crear_perfil(perfil: Perfil):
    return {
        "saludo":"Hola, {perfil.usuario}!",
        "bio": perfil.bio,
        "intereses": perfil.intereses
    }

@app.post("/calificacion/")
def validacion_estricta(datos: Estricto):
    return {"cantidad": datos.cantidad}

# Ejecutar la aplicación
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
