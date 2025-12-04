# 📦 Proyecto: sena-fastapi-actividad4

**Repositorio GitHub:** [https://github.com/heiderrevelo333/sena-fastapi-actividad4.git](https://github.com/heiderrevelo333/sena-fastapi-actividad4.git)

## 🚀 Descripción general

Este proyecto corresponde a la **Actividad 4 del curso de Python con FastAPI**.  
Su objetivo es practicar la creación de modelos Pydantic, manejo de rutas y validación de datos mediante el framework **FastAPI**.

La aplicación implementa múltiples endpoints que demuestran conceptos como:
- Campos opcionales en modelos.
- Conversión automática de tipos.
- Valores por defecto.
- Manejo de errores de validación (código 422).
- Respuestas JSON claras y tipadas.

---

## ⚙️ Requisitos previos

Antes de ejecutar el proyecto, asegúrate de tener instalado:

- Python 3.10 o superior  
- FastAPI  
- Uvicorn  

Puedes instalar las dependencias ejecutando:

```bash
pip install fastapi uvicorn
```

## ▶️ Ejecución del proyecto

Desde la terminal, en la carpeta raíz del proyecto, ejecuta:

```bash
uvicorn main:app --reload
```

Luego abre en tu navegador:
👉 http://localhost:8000/docs

Ahí podrás probar cada endpoint usando la interfaz interactiva Swagger UI.

## 🧩 Endpoints implementados
Método	Ruta	Descripción	Ejemplo de entrada	Ejemplo de salida
GET	/	Mensaje de bienvenida	–	{ "mensaje": "Bienvenido..." }
POST	/productos/	Crea un producto y devuelve sus datos	{ "nombre": "Teclado", "precio": 99.9, "en_stock": true, "tags": ["periférico"] }	Eco de los datos enviados
GET	/productos/buscar/?nombre=monitor&categoria=oficina	Búsqueda con parámetros de consulta	–	{ "nombre": "monitor", "categoria": "oficina" }
POST	/orden/	Recibe una orden y devuelve el total de ítems	{ "cliente": "Sofía", "items": ["A1", "B2"] }	{ "cliente": "Sofía", "total_items": 2 }
POST	/respuesta/	Detecta el tipo de dato recibido (int o str)	{ "valor": 123 }	{ "tipo": "int", "valor": 123 }
POST	/perfil/	Demuestra campos opcionales	{ "usuario": "leo", "bio": "hola" }	Incluye saludo y campos opcionales
POST	/calificacion/	Conversión automática de tipo float	{ "curso": "Python", "nota": "4.5" }	{ "curso": "Python", "nota": 4.5, "mensaje": "Calificación registrada para Python" }
POST	/configuracion/	Usa valores por defecto si no se envían datos	{}	{ "modo": "produccion", "version": 1.0 }
POST	/validacion/estricta	Valida tipos estrictamente	{ "cantidad": "abc" }	Error 422 Unprocessable Entity

## 🧠 Validaciones esperadas (para pruebas automáticas)

Ruta raíz / debe devolver exactamente { "mensaje": "Bienvenido..." }.

Rutas POST deben retornar JSON válido con claves esperadas.

En /calificacion/, si la nota se envía como texto "4.5", debe convertirse a float.

En /configuracion/, los valores por defecto deben aplicarse correctamente.

En /validacion/estricta, si se envía un valor no numérico, debe retornar HTTP 422.

## 📄 Estructura del proyecto

```
sena-fastapi-actividad4/
│
├── main.py          # Código principal de la aplicación FastAPI
├── README.md        # Descripción y documentación del proyecto
└── requirements.txt # Dependencias del proyecto
```

## 👨‍💻 Autor

Nombre: Esteban Revelo
Yojhann Vasquez
Jeffry Lopez
Programa: Análisis y Desarrollo de Software
Centro de Formación: SENA