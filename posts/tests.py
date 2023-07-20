from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Post


class UserTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testUser', password='testpassword')

    def test_register(self):
        url = reverse('register')
        data = {'username': 'testuser2', 'password': 'testpassword2'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

    def test_login(self):
        url = reverse('login')
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('logout')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class PostTests(APITestCase):
    def SetUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.post = Post.objects.create(title='Test Title', body='Test Body', user=self.user)

    def test_get_posts_list(self):
        url = reverse('posts')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        url = reverse('notes')
        data = {'title': 'Test Title 2', "body": 'Test Body 2', 'user': self.user}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_post_detail(self):
        url = reverse('post_detail', kwargs={'pk': self.post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_post(self):
        url = reverse('post_detail', kwargs={'pk': self.post.id})
        data = {'title': 'Updated Test Title', 'body': 'Updated Test body'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_post(self):
        url = reverse('post_detail', kwargs={'pk': self.post.id})
        data = {'pk': self.post.id}
        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
