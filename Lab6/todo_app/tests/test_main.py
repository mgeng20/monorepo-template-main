
from fastapi.testclient import TestClient
from src.main import app



client = TestClient(app)

# Test for GET request to /api


def test_get_first_api():
    response = client.get("/api")
    assert response.status_code == 200
    assert response.json() == {"msg": "hello_world"}

# Test for GET request to /books/{path_param}


def test_get_first_apiV2():
    response = client.get("/books/some_path_param")
    assert response.status_code == 200
    assert response.json() == {"msg": "some_path_param"}

# Test for GET request to /books/ with query parameter


def test_get_first_apiV3():
    response = client.get("/books/?title=BookTitle")
    assert response.status_code == 200
    assert response.json() == {"msg": "BookTitle"}




def test_get_first_apiV4():
    response = client.get("/books/create_book/Harry%20Potter?author=J.K%20Rowling")
    assert response.status_code == 200
    assert response.json() == {"msg": "new book Harry Potter author J.K Rowling"}

# Test for POST request to /api


def test_post_first_api():
    response = client.post("/api")
    assert response.status_code == 200
    assert response.json() == {"msg": "post api"}

# Test for PUT request to /api


def test_put_something():
    response = client.put("/api")
    assert response.status_code == 200
    assert response.json() == {"msg": "put api"}

# Test for DELETE request to /delete/something


def test_delete_something():
    response = client.delete("/delete/something")
    assert response.status_code == 200
    assert response.json() == {"success": True}
