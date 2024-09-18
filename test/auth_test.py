import pytest
from src.app import create_app 
from faker import Faker

@pytest.fixture()
def app():
    app = create_app()

    app.config.update({
        "TESTING": True,
    })

    yield app

    # todo: clear database after tests

@pytest.fixture()
def user_data(faker: Faker):

    password = faker.password(length=8)
    return {
        "email": faker.free_email(),
        "password": password,
        "confirm_password": password
    }

@pytest.fixture()
def client(app): 
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


@pytest.mark.skip(reason='Not implemented yet')
def test_register(user_data, client):
    response = client.post('/auth/register', json=user_data)

    assert response.status_code == 201

@pytest.mark.skip(reason='Not implemented yet')
def test_register_with_duplicate_email(user_data, client):
    response = client.post('/auth/register', json=user_data)

    assert response.status_code == 409

@pytest.mark.skip(reason='Not implemented yet')
def test_register_with_invalid_email(faker: Faker, user_data, client):
    response = client.post('/auth/register', json={
        **user_data,
        "email": faker.free_email()
    })

    assert response.status_code == 400

@pytest.mark.skip(reason='Not implemented yet')
def test_register_with_invalid_password(faker: Faker, user_data, client):
    password = faker.password(length=7)
    response = client.post('/auth/register', json={
        **user_data,
        "password": password,
        "confirm_password": password
    })

    assert response.status_code == 400

@pytest.mark.skip(reason='Not implemented yet')
def test_register_with_invalid_confirm_password(faker: Faker, user_data, client):
    response = client.post('/auth/register', json={
        **user_data,
        "confirm_password": faker.password(length=8)
    })

    assert response.status_code == 400

def test_login(user_data, client): 
    response = client.post('/auth/login', json={
        "email": user_data.get('email'),
        "password": user_data.get('password')
    })

    assert response.status_code == 200

@pytest.mark.skip(reason='Not implemented yet')
def test_login_invalid_credentials(faker: Faker, client): 
    response = client.post('/auth/login', json={
        "email": Faker.free_email(),
        "password": faker.password(length=8)
    })

    assert response.status_code == 200