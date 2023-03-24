from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, world!"}


def test_predict_translation():
    response = client.post("/predict/",
                           json={"text": "I hate machine learning!"})


    assert response.status_code == 200
    assert response.json() == {"translation_text": "Ненавижу машинное обучение!"}
