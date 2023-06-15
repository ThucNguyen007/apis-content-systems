import pytest

from rest_framework import status

from parent.fixtures.user import user

class TestAuthenticationViewSet:
    
    endpoint = '/api/auth/'
    
    # We are using the client fixture initialized in the conftest.py file 
    # to make a post request.
    # Then, we test for the value of status_code of the response and the response returned.
    def test_login(self, client, user):
        data = {
            "username": user.username,
            "password": "test_password"
        }
        response = client.post(self.endpoint + "login/", data)

        assert response.status_code == status.HTTP_200_OK
        assert response.data['access']
        assert response.data['user']['id'] == user.public_id.hex
        assert response.data['user']['username'] == user.username
        assert response.data['user']['email'] == user.email
    
    
    @pytest.mark.django_db    
    def test_register(self, client):
        data = {
            "username": "johndoe",
            "email": "johndoe@yopmail.com",
            "password": "test_password",
            "first_name": "John",
            "last_name": "Doe"
        }
        
        response = client.post(self.endpoint + "register/", data)
        assert response.status_code == status.HTTP_201_CREATED
        
    # within the test_refresh method, we log in to get a refresh token to make
    # a request to get a new access token.
    def test_refresh(self, client, user):
        data = {
            "username": user.username,
            "password": "test_password"
        }
        response = client.post(self.endpoint + "login/", data)

        assert response.status_code == status.HTTP_200_OK
        
        data_refresh = {
            "refresh":  response.data['refresh']
        }
        
        response = client.post(self.endpoint + "refresh/", data_refresh)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['access']