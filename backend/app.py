from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/saludo")
def saludo(nombre: str = "amigo"):
    return {
        "mensaje": f"Hola {nombre}, respuesta enviada desde el backend en EC2 🚀"
    }