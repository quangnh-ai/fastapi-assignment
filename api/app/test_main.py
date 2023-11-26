from fastapi.testclient import TestClient
import sys
sys.path.insert(0, "/app")

from core import security, config
from db import models
from db.session import session_local
from main import app
from requests_toolbelt.multipart.encoder import MultipartEncoder


client = TestClient(app)

def get_test_db_url() -> str:
    return f"{config.DATABASE_URL}_test"

#test_superuser
test_superuser = [
                {
                    "email": "admin@admin.com",
                    "first_name": "Admin",
                    "last_name": "Admin",
                    "is_active": True,
                    "is_superuser": True,
                    "id": 1
                }
                ]
# Gen superuser token
login_data = {
    "username": "admin@admin.com",
    "password": "admin",
}
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded'
}
r = client.post("/api/token", data=login_data, headers=headers)
tokens = r.json()
a_token = tokens["access_token"]
superuser_token_headers = {"Authorization": f"Bearer {a_token}"}
superuser_token_headers["accept"]="application/json"


# Test User
def test_create_user():
    superuser_token_headers['Content-Type']='application/json'
    new_user = {
                "email": "user_new",
                "first_name": "user_new",
                "last_name": "user_new",
                "is_active": True,
                "is_superuser": True,
                "password": "user_new"
                }
    response = client.post(
        "/api/v1/users/create", json=new_user, headers=superuser_token_headers
    )
    assert response.status_code == 201

def test_get_users():
    response = client.get("/api/v1/users/get?skip=0&limit=1", headers=superuser_token_headers)
    assert response.status_code == 200
    assert response.json() == test_superuser

def test_edit_user(user_id :int = 2):
    new_user = {
        "email": "newemail@email.com",
        "is_active": True,
        "is_superuser": False,
        "first_name": "Joe",
        "last_name": "Smith",
        "password": "1",
    }

    response = client.put(
        f"api/v1/users/update/{user_id}",
        json=new_user,
        headers=superuser_token_headers,
    )
    assert response.status_code == 200
    new_user["id"] = user_id
    new_user.pop("password")
    assert response.json() == new_user

def test_edit_user_not_found():
    new_user = {
        "email": "newemail@email.com",
        "is_active": False,
        "is_superuser": False,
        "password": "new_password",
    }
    response = client.put(
        "/api/v1/users/update/1234", json=new_user, headers=superuser_token_headers
    )
    assert response.status_code == 404
                  
def test_delete_user(user_id :int = 2):
    response = client.delete(
        f"/api/v1/users/delete/{user_id}", headers=superuser_token_headers
    )
    db = session_local()
    assert response.status_code == 200
    assert db.query(models.User).filter(models.User.id == user_id).first() == None

def test_delete_user_not_found():
    response = client.delete(
        "/api/v1/users/delete/4321", headers=superuser_token_headers
    )
    assert response.status_code == 404


# Test Auth
def verify_password_mock(first: str, second: str):
    return True


def test_login(monkeypatch):
    # Patch the test to skip password hashing check for speed
    monkeypatch.setattr(security, "verify_password", verify_password_mock)

    response = client.post(
        "/api/token",
        data={"username": test_superuser[0]['email'], "password": "nottheactualpass"},
    )
    assert response.status_code == 200


def test_signup(monkeypatch):
    def get_password_hash_mock(first: str, second: str):
        return True
    # superuser_token_headers['Content-Type']='application/x-www-form-urlencoded'
    superuser_token_headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    monkeypatch.setattr(security, "get_password_hash", get_password_hash_mock)

    response = client.post(
        "/api/signup",
        headers=superuser_token_headers,
        data={"username": "user_new", "password": "user_new"},
    )
    assert response.status_code == 200


# Test Book
def test_create_book():
    
    img_path = "/images/000000000.jpg"
    new_book = {
        "title": "IT-test-book",
        "author": "IT Man",
        "publish_date": "2023-01-21",
        "isbn": "1111111143",
        "price": 9.99
    }
    
    img_byte = MultipartEncoder(
        fields={'file': ('filename', open(img_path, 'rb'), 'image/jpeg')}
        )
    response = client.post(
        f"/api/v1/books/create",  json=new_book, data=img_byte, headers=superuser_token_headers
    )
    print(response.text)
    assert response.status_code == 201

def test_get_book_by_id(book_id: int = 1):
    response = client.get(
        f"/api/v1/books/get/id/{book_id}", headers=superuser_token_headers
    )
    assert response.status_code == 200

def test_edit_book(test_book, test_db, token):
    img_path = "/images/000000000.jpg"
    book_info = {
        "title": "IT Book",
        "author": "IT Man",
        "publish_date": "2023-01-01",
        "isbn": "111111111",
        "image_link": "http://localhost:8081/api/v1/books/show_image/?path=/images/111111111.jpg",
        "price": 9.99
    }
    
    img_byte = MultipartEncoder(
        fields={'file': ('filename', open(img_path, 'rb'), 'image/jpeg')}
        )
    
    response = client.put(
        f"/api/v1/books/{test_book.id}",  json=book_info, data=img_byte, headers=token
    )
    assert response.status_code == 200    

def test_delete_book(book_id: int = 3):
    response = client.delete(
        f"/api/v1/books/delete/{book_id}", headers=superuser_token_headers
    )
    assert response.status_code == 200