import pytest
from app import app


@pytest.fixture
def client():
    """Create a test client for the application.

    This fixture sets up the test client with the app's configuration set to
    TESTING mode.
    It then yields the client for use in test functions.
    """
    app.config['TESTING'] = True  # Set TESTING mode for the app configuration
    with app.test_client() as client:
        yield client  # Yield the test client for use in test functions


def test_main_page(client):
    """Test the main page of the application.

    This function tests the main page by sending a GET request to the root
    endpoint.
    It asserts that the response status code is 200 and the "Hello, World!"
    string is present in the response data.
    """
    response = client.get('/')  # Send a GET request to the root endpoint
    assert response.status_code == 200  # Assert the response status code is
    # 200 (OK)
    assert b'Hello, World!' in response.data  # Assert "Hello, World!" is
    # present in the response data
