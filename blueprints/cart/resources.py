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
    
    # Put
    @jwt_required
    def put(self, id):
        # validasi id gak ngaco
        if int(id) > 0:
            cart = Cart.query.get(id)
            if cart:
                parser = reqparse.RequestParser()
                parser.add_argument('stok', type=int, location='json', required=True, default = 1)
                args = parser.parse_args()

                cart.stok = args['stok']
                db.session.commit()
                cart = marshal(cart, Cart.cart_fields)
                app.logger.debug('DEBUG : %s', cart)
                    
                return cart, 200, {'Content-Type':'application/json'}
            return {'status' : 'NOT FOUND'}, 404, {'Content-Type':'application/json'}
        return {'status' : 'BAD REQUEST'}, 400, {'Content-Type':'application/json'}

class TotalPrice(Resource):
    @jwt_required
    def get(self):
        qry = Cart.query.all()
        total_harga = 0
        for query in qry:
            if query.status_cart == 1:
                total = total_harga + query.harga*query.stok
                total_harga = total
        return total_harga
        
class CartList(Resource):
    # Get All
    @jwt_required
    def get(self):
        qry = Cart.query.all()
        filter_result = []
        for query in qry:
            filter_result.append(marshal(query, Cart.cart_fields))
        return filter_result

class AddToCart(Resource):
    @jwt_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('status_cart', type=bool, location='json', required=True, default=False)
        parser.add_argument('book_id', location='json', required=True)
        parser.add_argument('judul', location='json', required=True)
        parser.add_argument('penulis', location='json', required=True)
        parser.add_argument('jenis_cover', location='json', required=True)
        parser.add_argument('foto_buku', location='json', required=True)
        parser.add_argument('harga', type=int, location='json', required=True)
        parser.add_argument('stok', type=int, location='json', required=True, default = 1)
        parser.add_argument('berat', type=int, location='json', required=True, default = 1)
        parser.add_argument('nama_lengkap', location='json', required=True)
        parser.add_argument('email', location='json', required=True)
        args = parser.parse_args()

        claim = get_jwt_claims()

        cart = Cart(args['status_cart'], claim['id'], args['book_id'], args['judul'], args['penulis'], args['jenis_cover'], args['foto_buku'], args['harga'], args['stok'], args['berat'], args['nama_lengkap'], args['email'])

        db.session.add(cart)
        db.session.commit()
        app.logger.debug('DEBUG : %s', cart)

        return marshal(cart, Cart.cart_fields), 200, {'Content-Type' : 'application/json'}

api.add_resource(TotalPrice,'/Total')
api.add_resource(AddToCart,'/Add')
api.add_resource(CartList, '/AllCart')
api.add_resource(CartResource, '/<id>')