import pytest, json, logging
from flask import Flask, request

from blueprints import app, db
from blueprints.book.model import Books
from blueprints.cart.model import Cart
from blueprints.user.model import User
from app import cache

# Password Encription
from password_strength import PasswordPolicy
import hashlib

def db_reset():
    db.drop_all()
    db.create_all()

    password_1 = hashlib.md5("l3l11234".encode()).hexdigest()
    user1 = User('Lelianto', 'lian@alterra.id', password_1,'None','None','None','None')
    db.session.add(user1)
    db.session.commit()

    password_2 = hashlib.md5("l3l1123456".encode()).hexdigest()
    user2 = User('Lelianto', 'lelianto.eko@gmail.com', password_2,'None','None','None','None')
    db.session.add(user2)
    db.session.commit()

def call_client(request):
    client = app.test_client()
    return client

@pytest.fixture
def client(request):
    return call_client(request)

def create_token(isInternal):
    # Checking whether internal or not and prepare the data
    if isInternal:
        cachename = "test-internal-token"
        data = {
            'email': 'lian@alterra.id',
            'kata_sandi': 'l3l11234'
        }
    else:
        cachename = "test-non-internal-token"
        data = {
            'email': 'lelianto.eko@gmail.com',
            'kata_sandi': 'l3l1123456'
        }

    token = cache.get(cachename)
    if token is None:
        # Do Request
        req = call_client(request)
        res = req.post('/token', json = data, content_type='application/json')

        # Store Response
        res_json = json.loads(res.data)

        logging.warning('RESULT : %s', res_json)

        # Assertion
        assert res.status_code == 200

        # Save token into cache
        cache.set(cachename, res_json['token'], timeout = 60)

        # Return, because it is useful for other test
        return res_json['token']
    else:
        return token