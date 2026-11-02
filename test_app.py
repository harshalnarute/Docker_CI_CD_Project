from fastapi.testclient import TestClient

from app import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()['status'] == "Healthy"
    
def test_prediction():
    response = client.post(
        "/predict",
        json={'study_hours':6}
    )
    assert response.status_code == 200
    assert response.json()['predicted_score'] == 68.0
    
    
def test_score():
    response = client.post(
        "/predict",
        json = {'study_hours' : 30} 
    )
    assert response.status_code == 422
    
    
    
    