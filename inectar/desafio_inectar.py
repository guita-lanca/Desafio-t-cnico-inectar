# Desafio técnico INECTAR

import json
import os

ARQUIVO = "favoritos.json"

class Jogo: 
    def __init__(self, nome: str, nota: float, id: int):
        self.nome = nome
        self.nota = nota
        self.id = id

    @staticmethod
    def montar_objeto(jogo_dict: dict):
        return Jogo(
            nome=jogo_dict.get('nome'),
            nota=jogo_dict.get('nota'),
            id=jogo_dict.get('id')
        )

    def montar_dict(self):
        return {
            'nome': self.nome,
            'nota': self.nota,
            'id': self.id
        }
    
def carregar_dados():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_dados(lista):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=4, ensure_ascii=False)

def adicionar_jogo(jogo: dict):
    lista_jogos = carregar_dados()
    lista_jogos.append(jogo)
    salvar_dados(lista_jogos)

def editar_jogos(jogo: dict, jogo_id: int):
    lista_jogos = carregar_dados()
    for i, jogo_item in enumerate(lista_jogos):
        if jogo_item.get('id') == jogo_id:
            lista_jogos[i].update(jogo)
            salvar_dados(lista_jogos)
            return
    # se não encontrar, só ignora
    return

def remover_jogo(jogo_id: int):
    lista_jogos = carregar_dados()
    for i, jogo_item in enumerate(lista_jogos):
        if jogo_item.get('id') == jogo_id:
            lista_jogos.pop(i)
            salvar_dados(lista_jogos)
            return
    # se não encontrar, só ignora
    return

