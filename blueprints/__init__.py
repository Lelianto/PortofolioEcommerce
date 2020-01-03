# Import
import json, os
from flask import Flask, request, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_jwt_extended import JWTManager, verify_jwt_in_request, get_jwt_claims

# Others
from datetime import timedelta
from functools import wraps

app = Flask(__name__)

app.config['APP_DEBUG'] = True

# JWT Setup
app.config['JWT_SECRET_KEY'] = 'iuahdLIXwaDOIXhodihowdoqd'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days = 1)
jwt = JWTManager(app)

def internal_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_claims()

        if claims['email'] != 'lian@alterra.id':
            return {'status': 'FORBIDDEN', 'message': 'Internal Only'}, 403
        else:
            return fn(*args, **kwargs)
    return wrapper

env = os.environ.get('FLASK_ENV', 'development')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@0.0.0.0:3306/test_porto' if (env == 'testing') else 'mysql+pymysql://root:@0.0.0.0:3306/porto'  
  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Form app.py
@app.after_request
def after_request(response):
    try:
        requestData = request.get_json()
    except Exception as e:
        requestData = request.args.to_dict()
    if response.status_code == 200:
        app.logger.info("REQUEST_LOG\t%s", json.dumps({
            'status_code': response.status_code,
            'method': request.method,
            'code': response.status,
            'url': request.full_path,
            'request': requestData,
            'response': json.loads(response.data.decode('utf-8'))
        }))
    else:
        app.logger.error("REQUEST_LOG\t%s", json.dumps({
            'status_code': response.status_code,
            'method': request.method,
            'code': response.status,
            'url': request.full_path,
            'request': requestData,
            'response': json.loads(response.data.decode('utf-8'))
        }))
    return response

# # Endpoint untuk create token
from blueprints.auth.__init__ import bp_auth
app.register_blueprint(bp_auth, url_prefix='/token')

# Endpoint untuk CRUD user
from blueprints.user.resources import bp_user
app.register_blueprint(bp_user, url_prefix = '/user')

# Endpoint untuk CRUD book
from blueprints.book.resources import bp_book
app.register_blueprint(bp_book, url_prefix = '/book')

# Endpoint untuk CRUD cart
from blueprints.cart.resources import bp_cart
app.register_blueprint(bp_cart, url_prefix = '/cart')

# Endpoint untuk CRUD cart
from blueprints.payment.resources import bp_payment
app.register_blueprint(bp_payment, url_prefix = '/payment')

# db.create_all()



