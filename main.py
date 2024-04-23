from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from starlette.middleware.cors import *

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

restaurantes = [
    {"nome": "Restaurante da tia Teteia", "status": "ativo"},
    {"nome": "Cantinho do Sabor", "status": "ativo"},
    {"nome": "Sabor Familiar", "status": "ativo"},
    {"nome": "Rancho da Vovó", "status": "ativo"},
    {"nome": "Sabor Caseiro", "status": "ativo"},
    {"nome": "Casa do Paulo", "status": "inativo"},
]


@app.get("/restaurantes/")
def listar_restaurantes():
    return restaurantes


if __name__ == "__main__":
    uvicorn.run(app, port=8080)
