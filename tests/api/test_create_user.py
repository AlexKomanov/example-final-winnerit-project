import pytest
import re
from api_requests.users_request import UsersRequest

@pytest.fixture
def user_request():
    """Fixture that returns a UsersRequest instance"""
    return UsersRequest()

def test_create_user_success(user_request):
    """Test successful user creation"""
    # Test data
    user_data = {
        "name": "morpheus",
        "job": "leader"
    }
    
    response = user_request.create_user(user_data["name"], user_data["job"])
    data = response.json()
    
    # Verify status code
    assert response.status_code == 201
    
    # Verify response structure and values
    assert data["name"] == user_data["name"]
    assert data["job"] == user_data["job"]
    assert "id" in data
    assert "createdAt" in data
    
    # Validate createdAt timestamp format
    timestamp_pattern = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$'
    assert re.match(timestamp_pattern, data["createdAt"]) is not None


    
