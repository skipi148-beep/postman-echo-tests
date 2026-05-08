import requests
import pytest

BASE_URL = "https://postman-echo.com"

def test_get_request_status():
    """Проверка GET-запроса: статус код 200"""
    response = requests.get(f"{BASE_URL}/get")
    assert response.status_code == 404

def test_get_with_params():
    """Проверка GET-запроса с параметрами"""
    params = {"foo1": "bar1", "foo2": "bar2"}
    response = requests.get(f"{BASE_URL}/get", params=params)
    
    data = response.json()
    assert data["args"]["foo1"] == "bar1"
    assert data["args"]["foo2"] == "bar2"

def test_post_raw_text():
    """Проверка POST-запроса с передачей обычного текста (Raw)"""
    payload = "This is expected to be sent back as part of response body."
    response = requests.post(f"{BASE_URL}/post", data=payload)
    
    assert response.status_code == 200
    assert response.json()["data"] == payload

def test_post_json():
    """Проверка POST-запроса с JSON-телом"""
    payload = {"test": "value"}
    response = requests.post(f"{BASE_URL}/post", json=payload)
    
    assert response.status_code == 200
    assert response.json()["json"] == payload

def test_headers_check():
    """Проверка передачи кастомных заголовков"""
    headers = {"my-sample-header": "test-value"}
    response = requests.get(f"{BASE_URL}/get", headers=headers)
    
    # Postman Echo возвращает все пришедшие заголовки в ключе 'headers'
    assert response.json()["headers"]["my-sample-header"] == "test-value"
