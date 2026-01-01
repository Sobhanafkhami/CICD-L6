import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_read_root():
    res = client.get('/')
    assert res.status_code == 200
    assert res.json() == {'hello':'world'}

def test_read_book():
    res = client.get('/book/1')
    assert res.status_code == 200
    assert res.json() == {'book_id': 1}

def test_read_book_not_found():
    res = client.get('/book/11')
    assert res.status_code == 404
    assert res.json() == {'detail': 'Book not found'}