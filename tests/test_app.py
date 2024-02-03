import pytest
from fastapi.testclient import TestClient

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


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == 200
    assert response.json() == {
        'users': [
            {
                'username': 'alice',
                'email': 'alice@example.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }


def test_update_user_not_found(client):
    response = client.put(
        '/users/2',
        json={
            'username': 'morgs',
            'email': 'morgs@example.com',
            'password': 'morgs',
        },
    )

    assert response.status_code == 404
    assert response.json() == {'detail': 'User not found'}


def test_delete(client):
    response = client.delete('/users/1')

    assert response.status_code == 200
    assert response.json() == {'message': 'você foi eliminaaade'}


def test_delete_user_not_found(client):
    response = client.delete('/users/2')

    assert response.status_code == 404
    assert response.json() == {'detail': 'User not found'}
