from rest_framework.test import APIClient
from datetime import datetime
from django.urls import reverse
from accounts.models import User
import pytest


@pytest.fixture
def api_client():
    client = APIClient()
    return client

@pytest.fixture
def common_user():
    user = User.objects.create_user(email='test@gmail.com',password='12345/@a')
    return user

# Create your tests here.
@pytest.mark.django_db
class TestPostApi:

    def test_get_posts_response_200_status(self,api_client):
        url = reverse("blog:api-v1:post-list")
        response = api_client.get(url)
        assert response.status_code == 200
    
    def test_create_post_response_401_status(self,api_client):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title" : "test",
            "content" : "descriptions",
            "status" : True,
            "published_at" : datetime.now()
        }
        response = api_client.post(url,data)
        assert response.status_code == 401
    
    def test_create_post_response_201_status(self,api_client,common_user):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title" : "test",
            "content" : "descriptions",
            "status" : True,
            "published_at" : datetime.now()
        }
        user = common_user
        api_client.force_authenticate(user=user)
        response = api_client.post(url,data)
        assert response.status_code == 201
    def test_create_post_invalid_data_response_400_status(self,api_client,common_user):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title" : "test",
            "content" : "descriptions"
        }
        user = common_user
        api_client.force_authenticate(user=user)
        response = api_client.post(url,data)
        assert response.status_code == 400
