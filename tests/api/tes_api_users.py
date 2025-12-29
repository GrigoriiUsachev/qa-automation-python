import requests
import pytest
pytestmark = pytest.mark.api

def test_get_user():
    response = requests.get("https://reqres.in/api/users/2")

    assert response.status_code == 200
    body = response.json()
    assert body["data"]["id"] == 2


def test_create_user():
    payload = {
        "name": "Gregory",
        "job": "QA Engineer"
    }

    response = requests.post(
        "https://reqres.in/api/users",
        json=payload
    )

    assert response.status_code == 201
    assert response.json()["name"] == "Gregory"