from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_predict_endpoint():
    sample_input = {
        "CreditScore": 650,
        "Age": 45,
        "Tenure": 5,
        "Balance": 50000.0,
        "NumOfProducts": 2,
        "HasCrCard": 1,
        "IsActiveMember": 1,
        "EstimatedSalary": 70000.0,
        "Geography": "France",
        "Gender": "Male"
    }

    response = client.post("/predict", json=sample_input)
    assert response.status_code == 200
    assert "churn_prediction" in response[0].json()
    assert "churn_probability" in response[0].json()
