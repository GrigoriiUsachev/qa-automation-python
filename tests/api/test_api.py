import requests


def test_get_post():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

    assert response.status_code == 200
    body = response.json()
    assert body["id"] == 1


def test_create_post():
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }

    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=payload
    )

    assert response.status_code == 201
    assert response.json()["title"] == "foo"