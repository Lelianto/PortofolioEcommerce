# Import
from flask import Blueprint
from flask_restful import Api, reqparse, Resource, marshal, inputs
from datetime import datetime
from sqlalchemy import desc
from .model import Cart
from blueprints import db, app
from datetime import datetime
import json

# Import Authentication
from flask_jwt_extended import jwt_required, get_jwt_claims
from blueprints import internal_required

# kata_sandi Encription
from password_strength import PasswordPolicy
import hashlib

# Creating blueprint
bp_cart = Blueprint('cart', __name__)
api = Api(bp_cart)

class CartResource(Resource):
    def __init__(self):
        pass
    
    def options(self, id=None):
        return {"status":"ok"},200

    @jwt_required
    def get(self, id=None):
        qry = Cart.query.get(id)
        if qry is not None:
          return marshal(qry, Cart.cart_fields), 200, {'Content-Type' : 'application/json'}
        return {'status' : 'NOT_FOUND'}, 404

    # Delete
    @jwt_required
    def delete(self, id):
        user = User.query.get(id)

        if user is not None:
            # Hard Delete
            db.session.delete(user)
            db.session.commit()
            return {'status': 'DELETED'}, 200, {'Content-Type':'application/json'}
        return {'status' : 'NOT FOUND'}, 404, {'Content-Type':'application/json'}

class CartList(Resource):
    # Get All
    @jwt_required
    def get(self):
        qry = User.query.all()
        filter_result = []
        for query in qry:
            filter_result.append(marshal(query, User.user_fields))
        return filter_result
    
    @jwt_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('total_beli', location='args', required=True)
        args = parser.parse_args()

        claim = get_jwt_claims()

        cart = Cart(claim['user_id'], claim['book_id'], args['total_beli'], claim['total_harga'], claim['status_cart'], claim['judul'], claim['penulis'], claim['jenis_cover'], claim['foto_buku'], claim['harga'], claim['stok'], claim['nama_lengkap'], claim['email'])

        db.session.add(cart)
        db.session.commit()

        app.logger.debug('DEBUG : %s', cart)

        return marshal(keranjang, Cart.response_fields), 200, {'Content-Type' : 'application/json'}

class AddToCart(Resource):
    @jwt_required
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('book_id', location='json', required=True)
        parser.add_argument('total_beli', location='json', default=1, required=True)
        parser.add_argument('foto_buku', location='json', required=True)

        parser.add_argument('judul', location='json', required=True)
        parser.add_argument('penulis', location='json', required=True)
        parser.add_argument('jenis_cover', location='json', required=True)
        parser.add_argument('foto_buku', location='json', required=True)
        parser.add_argument('harga', location='json', required=True)
        args = parser.parse_args()

        claim = get_jwt_claims()

        cart = Cart(claim['id'], args['book_id'], args['total_beli'], args['total_harga'], args['status_cart'], args['judul'], args['penulis'], args['jenis_cover'], args['foto_buku'], args['harga'], args['stok'], args['nama_lengkap'], args['email'])

        db.session.add(cart)
        db.session.commit()

        app.logger.debug('DEBUG : %s', cart)

        return marshal(keranjang, Cart.response_fields), 200, {'Content-Type' : 'application/json'}

api.add_resource(AddToCart,'/Add')
api.add_resource(CartList, '')
api.add_resource(CartResource, '/<id>')