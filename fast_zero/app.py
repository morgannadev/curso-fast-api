from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message

app = FastAPI()


# o status_code 200 é padrão para rotas get
@app.get('/', status_code=200, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


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
