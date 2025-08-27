from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from desafio_inectar import Jogo, carregar_dados, adicionar_jogo, editar_jogos, remover_jogo

app = FastAPI(title="API Jogos Favoritos", version="1.0")

# Modelo de entrada baseado no Pydantic
class JogoSchema(BaseModel):
    nome: str
    nota: float
    id: int

    def to_model(self) -> Jogo:
        return Jogo(nome=self.nome, nota=self.nota, id=self.id)

@app.get("/jogos", response_model=List[JogoSchema])
def listar_jogos():
    dados = carregar_dados()
    return [Jogo.montar_objeto(jogo).montar_dict() for jogo in dados]

@app.post("/jogos", response_model=JogoSchema)
def criar_jogo(jogo: JogoSchema):
    novo_jogo = jogo.to_model()
    adicionar_jogo(novo_jogo.montar_dict())
    return novo_jogo.montar_dict()

@app.put("/jogos/{jogo_id}", response_model=JogoSchema)
def atualizar_jogo(jogo_id: int, jogo: JogoSchema):
    jogos = carregar_dados()
    existe = any(item["id"] == jogo_id for item in jogos)
    if not existe:
        raise HTTPException(status_code=404, detail="Jogo não encontrado")

    novo_jogo = jogo.to_model()
    editar_jogos(novo_jogo.montar_dict(), jogo_id)
    return novo_jogo.montar_dict()

@app.delete("/jogos/{jogo_id}")
def deletar_jogo(jogo_id: int):
    jogos = carregar_dados()
    existe = any(item["id"] == jogo_id for item in jogos)
    if not existe:
        raise HTTPException(status_code=404, detail="Jogo não encontrado")

    remover_jogo(jogo_id)
    return {"mensagem": "Jogo removido com sucesso!"}

