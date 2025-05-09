from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, RequestsClient, APIRequestFactory, force_authenticate
from .views import AuthorListCreate, BookListCreate
from django.test import TestCase
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User


class AuthorTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_list_authors(self):
        response = self.client.get(reverse('author-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_author(self):
        response = self.client.post(reverse('author-list'), {'name': 'test_name', 'nationality': 'georgian'}, format='json') 
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_error(self):
        response = self.client.post(reverse('author-list'), {'nationality': 'georgian'}, format='json') 
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class BookTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='admin', password='admin')
        self.token = RefreshToken.for_user(self.user)

    def test_list_book_unauth(self):
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_book_auth(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token.access_token}')
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class BookListTestWithRequestClient(TestCase):
    def setUp(self):
        self.client = RequestsClient()
        self.user = User.objects.create_user(username='admin', password='admin')
        self.token = RefreshToken.for_user(self.user)
        self.client.headers.update({'Authorization': f'Bearer {self.token.access_token}'})

    def test_list_books(self):
        response = self.client.get('http://127.0.0.1:8000/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)