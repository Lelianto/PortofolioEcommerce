# Import
from flask import Blueprint
from flask_restful import Api, reqparse, Resource, marshal, inputs
from datetime import datetime
from sqlalchemy import desc
from .model import Payment
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
bp_payment = Blueprint('payment', __name__)
api = Api(bp_payment)

class PaymentList(Resource):
    
    # Post
    @jwt_required
    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument('nama_jalan', location='args', required=True)
        parser.add_argument('rt_rw', location='args', required=True)
        parser.add_argument('kelurahan', location='args', required=True)
        parser.add_argument('kecamatan', location='args', required=True)
        parser.add_argument('kota_kabupaten', location='args', required=True)
        parser.add_argument('provinsi', location='args', required=True)
        parser.add_argument('kode_pos', location='args', required=True)
        parser.add_argument('nomor_telepon', location='args', required=True)
        parser.add_argument('jasa_pengiriman', location='args', required=True)
        args = parser.parse_args()

        # claim = get_jwt_claims()

        payment = Payment(args['nama_jalan'], args['rt_rw'], args['kelurahan'], args['kecamatan'], args['kota_kabupaten'], args['provinsi'], args['kode_pos'], args['nomor_telepon'], args['jasa_pengiriman'])

        db.session.add(payment)
        db.session.commit()

        app.logger.debug('DEBUG : %s', payment)

        return marshal(keranjang, Payment.response_fields), 200, {'Content-Type' : 'application/json'}

api.add_resource(PaymentList, '')