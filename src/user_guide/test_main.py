from fastapi.testclient import TestClient   
from fastapi import status
# import sys
# from pathlib import Path

# sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from user_guide.staticFiles_testing_debugging import app


client = TestClient(app)

def test_read_item():
    response = client.get("/items/foo", headers={"X-Token": "coneofsilence"})
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "id": "foo",
        "title": "Foo",
        "description": "There goes my hero",
    }


def test_read_item_bad_token():
    response = client.get("/items/too", headers={"X-Token": "wrong"})
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {"detail": "Invalid X-Token header"}

def test_read_inexisting_item():
    response = client.get("/items/baz", headers={"X-Token": "coneofsilence"})
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "item not found"}

def test_create_item():
    response = client.post(
        "/items/",
        json = {"id": "foobar", "title": "Foo Bar", "description": "The Foo Bartender"},
        headers={"X-Token": "coneofsilence"},
    )
    assert response.status_code==status.HTTP_201_CREATED
    assert response.json() == {
        "id":"foobar",
        "title": "Foo Bar",
        "description": "The Foo Bartender",

    }

def test_create_item_bad_token():
    response = client.post(
        "/items/",
        headers={"X-Token": "badheader"}, 
        json={"id":"bazz", "title": "Bazz", "description":"drop the bazz"}
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {"detail": "Invalid X-Token header"}


def test_create_existing_item():
    response = client.post("/items/",
        headers={"X-Token": "coneofsilence"}, 
        json={"id":"foo", "title": "Bazz", "description":"drop the bazz"})
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {"detail": "item already exists"}
