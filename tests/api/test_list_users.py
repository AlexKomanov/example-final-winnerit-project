import pytest
from api_requests.users_request import UsersRequest

@pytest.fixture
def user_request():
    """Fixture that returns a UsersRequest instance"""
    return UsersRequest()

def test_list_users_status_code(user_request):
    """Test that the users endpoint returns 200 OK"""
    response = user_request.list_users()
    assert response.status_code == 200

def test_list_users_page_parameter(user_request):
    """Test pagination functionality"""
    response = user_request.list_users(page=2)
    data = response.json()
    
    assert response.status_code == 200
    assert data["page"] == 2
    assert data["per_page"] == 6
    assert data["total"] == 12
    assert data["total_pages"] == 2

def test_list_users_data_structure(user_request):
    """Test the structure of user data in the response"""
    response = user_request.list_users(page=2)
    data = response.json()
    
    # Verify we have the expected number of users
    assert len(data["data"]) == 6
    
    # Verify the structure of a user object
    user = data["data"][0]
    assert all(key in user for key in ["id", "email", "first_name", "last_name", "avatar"])

def test_list_users_invalid_page(user_request):
    """Test response with invalid page number"""
    response = user_request.list_users(page=999)
    data = response.json()
    
    assert response.status_code == 200
    assert len(data["data"]) == 0

@pytest.mark.parametrize("user_id", [7, 8, 9, 10, 11, 12])
def test_specific_users_on_page_two(user_request, user_id):
    """Test that specific users exist on page 2"""
    response = user_request.list_users(page=2)
    data = response.json()
    
    user_ids = [user["id"] for user in data["data"]]
    assert user_id in user_ids
