import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    idade: int
    ativo: bool = True

@app.get(path="/saudar/{nome}")
async def saudar(nome: str):
    return {"mensagem:" f"Olá, {nome}"}

@app.post(path="/usuarios")
async def criar_usuario(user: User):
    return {
        "mensagem": "Usuário criado!",
        "dados": dict(user)
    }

if __name__== "__main__":
    uvicorn.run(
        "app:app",
        host="localhost",
        port=3001,
        reload=True
    )