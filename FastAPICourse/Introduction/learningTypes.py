from pydantic import BaseModel

class User(BaseModel):
    name: str
    idade: int
    ativo: bool = True

try:
    user = User(name="Gustavo", idade=21)
    print(user)
except Exception as e:
    print("Erro de validação")
    print(e)