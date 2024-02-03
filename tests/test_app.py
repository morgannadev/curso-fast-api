from fastapi.testclient import TestClient
import pytest

from fast_zero.app import app


# técnica DRY: don't repeat yourself
@pytest.fixture   # Arrange
def client():
    return TestClient(app)


# criado com a técnica AAA (Arrange, Act, Assert)
def test_root_deve_retornar_200_e_ola_mundo(client):
    response = client.get('/')   # Act

    assert response.status_code == 200   # Assert
    assert response.json() == {'message': 'Olá Mundo!'}   # Assert


def test_olamundo_deve_retornar_200_e_ola_mundo_em_html(client):
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


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == 201
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@example.com',
        'id': 1,
    }
