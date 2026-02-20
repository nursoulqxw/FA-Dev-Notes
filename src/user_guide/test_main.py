from fastapi.testclient import TestClient   
# import sys
# from pathlib import Path

# sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from user_guide.staticFiles_testing_debugging import app


client = TestClient(app)

def test_read_item():
    response = client.get("/items/foo", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    assert response.json() == {
        "id": "foo",
        "title": "Foo",
        "description": "There goes my hero",
    }


def test_read_item_bad_token():
    response = client.get("/items/too", headers={"X-Token": "wrong"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid X-Token header"}

def test_read_inexisting_item():
    response = client.get("/items/baz", headers={"X-Token", "coneofsilence"})
    assert response.status_cide == 404
    assert response.json() == {"detail": "item not found"}

def test_create_item():
    ...