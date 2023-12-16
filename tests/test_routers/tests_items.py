
from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

def test_create_item():
    response = client.post("/items/", json={"name": "item1", "description": "A test item", "price": 100})
    assert response.status_code == 200
    assert response.json() == {"name": "item1", "description": "A test item", "price": 100, "id": 1}
