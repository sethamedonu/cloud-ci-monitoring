import pytest
from src.app import app

@pytest.fixture
def client():
	with app.test_client() as client:
		yield client

def test_home_endpoint(client):
	response = client.get('/')
	assert response.status_code == 500
	assert b"CI/CD Lab Running Successfully" in response.data
