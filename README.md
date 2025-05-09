# Testing-Django

## Description
Testing-Django is a Django REST Framework (DRF) project that provides APIs for managing authors and books. The project implements JWT authentication using `djangorestframework-simplejwt` and includes test cases for API endpoints.

## Features
- JWT authentication for secure API access
- Endpoints to create and list authors and books
- Test cases using `APIClient` and `RequestsClient`
- Django Admin integration

## Installation
1. Clone the repository:
   git clone https://github.com/anageguchadze/Testing-Django.git
   cd Testing-Django
   
2. Create a virtual environment and activate it:
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt
   
4. Apply migrations:
   python manage.py migrate
   
5. Create a superuser (optional, for admin access):
   python manage.py createsuperuser
   
6. Run the development server:
   python manage.py runserver
 

## API Endpoints
| Method | Endpoint        | Description              | Authentication |
|--------|---------------|--------------------------|----------------|
| GET    | /api/authors/ | List all authors        | None           |
| POST   | /api/authors/ | Create a new author     | None           |
| GET    | /api/books/   | List all books          | JWT Required   |
| POST   | /api/books/   | Create a new book       | JWT Required   |

## Running Tests
Run the test suite with:
python manage.py test


## Authentication
1. Obtain an access token:
   curl -X POST http://127.0.0.1:8000/api/token/ -d "username=admin&password=admin"
   
2. Use the token in requests:
   curl -H "Authorization: Bearer <your_token>" http://127.0.0.1:8000/api/books/


## License
This project is licensed under the MIT License.

