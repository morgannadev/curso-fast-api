from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message, UserDB, UserPublic, UserSchema

app = FastAPI()
database = []   # lista para ser um banco de dados provisório


# o status_code 200 é padrão para rotas get
@app.get('/', status_code=200, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


# rota feita para exercício
@app.get('/olamundo', status_code=200, response_class=HTMLResponse)
def olamundo():
    return """
    <html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>
    """


@app.post('/users/', status_code=201, response_model=UserPublic)
def create_user(user: UserSchema):
    # ** (unpacking ou desempacotamento)
    # é para desempacotar o json na chamada da função
    # user é o objeto que estamos recebendo
    # model_dump é para fazer a serialização
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)
    database.append(user_with_id)

    return user_with_id
