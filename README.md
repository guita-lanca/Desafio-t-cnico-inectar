# API Jogos Favoritos

Aplicação desenvolvida em **Python** com **FastAPI** para gerenciar uma lista de jogos favoritos.  
A API permite **cadastrar, listar, editar e remover jogos**, com os dados sendo armazenados em um arquivo `favoritos.json`.
---

## Tecnologias utilizadas
- FastAPI
- Uvicorn

---

##  Estrutura do projeto
```
├── desafio_inectar.py   # Script com as funções de manipulação dos dados
├── main.py              # API principal usando FastAPI
├── favoritos.json       # Arquivo onde os jogos são armazenados (criado automaticamente)
└── README.md            # Documentação do projeto
```

---

##  Como instalar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/jogos-favoritos.git
   cd jogos-favoritos
   ```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install fastapi uvicorn
   ```

---

##  Como executar

Execute o servidor local com:
```bash
uvicorn main:app --reload
```

A API estará disponível em:  
 [http://127.0.0.1:8000](http://127.0.0.1:8000)

E a documentação interativa do FastAPI estará em:  
 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

##  Endpoints disponíveis

###  Listar jogos
```
GET /jogos
```
Retorna a lista de jogos cadastrados.

---

###  Criar jogo
```
POST /jogos
```
**Exemplo de corpo da requisição:**
```json
{
  "nome": "The Witcher 3",
  "nota": 9.8,
  "id": 1
}
```

---

###  Atualizar jogo
```
PUT /jogos/{jogo_id}
```
**Exemplo de corpo da requisição:**
```json
{
  "nome": "The Witcher 3 - Edição Completa",
  "nota": 10,
  "id": 1
}
```

---

###  Deletar jogo
```
DELETE /jogos/{jogo_id}
```
Remove o jogo pelo **id** informado.

---

##  Persistência dos dados
Os dados são armazenados em um arquivo `favoritos.json`, que é criado automaticamente na raiz do projeto na primeira execução da API.

---
