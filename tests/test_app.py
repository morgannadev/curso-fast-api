from fast_zero.schemas import UserPublic


# criado com a técnica AAA (Arrange, Act, Assert)
def test_root_deve_retornar_200_e_ola_mundo(client):
    response = client.get('/')   # Act

    assert response.status_code == 200   # Assert
    assert response.json() == {'message': 'Olá Mundo!'}   # Assert


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


def test_create_user_already_registered(client, user):
    response = client.post(
        '/users/',
        json={
            'username': 'Teste',
            'email': 'test@test.com',
            'password': 'testtest',
        },
    )

    assert response.status_code == 400
    assert response.json() == {'detail': 'Username already registered'}


def test_read_users(client):
    response = client.get('/users')

    assert response.status_code == 200
    assert response.json() == {'users': []}


def test_read_users_with_users(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users/')
    assert response.json() == {'users': [user_schema]}


def test_update_user(client, user):
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


# neste caso não precisamos passar user porque estamos testando 404
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


def test_delete_user(client, user):
    response = client.delete('/users/1')

    assert response.status_code == 200
    assert response.json() == {'message': 'User deleted'}


# neste caso não precisamos passar user porque estamos testando 404
def test_delete_user_not_found(client):
    response = client.delete('/users/2')

    assert response.status_code == 404
    assert response.json() == {'detail': 'User not found'}


def test_read_user(client, user):
    response = client.get('/users/1')

    assert response.status_code == 200
    assert response.json() == {
        'id': 1,
        'username': 'Teste',
        'email': 'test@test.com',
    }


# neste caso não precisamos passar user porque estamos testando 404
def test_read_user_not_found(client):
    response = client.get('/users/2')

    assert response.status_code == 404
    assert response.json() == {'detail': 'User not found'}
