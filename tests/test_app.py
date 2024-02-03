from fastapi.testclient import TestClient

from fast_zero.app import app

client = TestClient(app)   # Arrange

# criado com a técnica AAA (Arrange, Act, Assert)
def test_root_deve_retornar_200_e_ola_mundo():
    response = client.get('/')   # Act

    assert response.status_code == 200   # Assert
    assert response.json() == {'message': 'Olá Mundo!'}   # Assert


def test_olamundo_deve_retornar_200_e_ola_mundo_em_html():
    response = client.get('/olamundo')

    assert response.status_code == 200
    assert (
        response.text
        == """
    <html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>
    """
    )
