from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_suma():
    client = app.test_client()
    response = client.get("/suma/5/3")
    data = response.get_json()
    assert data["resultado"] == 8
