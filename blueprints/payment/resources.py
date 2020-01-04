# Import
from flask import Blueprint
from flask_restful import Api, reqparse, Resource, marshal, inputs
from datetime import datetime
from sqlalchemy import desc
from .model import Payment
from blueprints import db, app
from datetime import datetime
from blueprints.cart.model import Cart
import json
import requests

# Import Authentication
from flask_jwt_extended import jwt_required, get_jwt_claims
from blueprints import internal_required

# kata_sandi Encription
from password_strength import PasswordPolicy
import hashlib

# Creating blueprint
bp_payment = Blueprint('payment', __name__)
api = Api(bp_payment)

# class PaymentList(Resource):
    

class Expedition(Resource):

    RAJAONGKIR_API_KEY = 'c34f8ffa7ae33fa06c280cf1a0a01589'
    RAJAONGKIR_COST_API = 'https://api.rajaongkir.com/starter/cost'
    RAJAONGKIR_CITY_API = 'https://api.rajaongkir.com/starter/city'
    DEFAULT_COURIER = 'jne'

    def GetIdKota(self, kota_kabupaten):
        req_kota = requests.get(self.RAJAONGKIR_CITY_API, params={'key': self.RAJAONGKIR_API_KEY})
        result = req_kota.json()

        list_kota = result['rajaongkir']['results']
        for kota in list_kota:
            if kota['city_name'].lower() == kota_kabupaten.lower():
                return int(kota['city_id'])

    def GetBiayaPengiriman(self, kota_asal, kota_tujuan, berat_gram):
        kota_asal_id = self.GetIdKota(kota_asal)
        kota_tujuan_id = self. GetIdKota(kota_tujuan)

        req = requests.post(self.RAJAONGKIR_COST_API, json={'key': self. RAJAONGKIR_API_KEY, 'origin':kota_asal_id, 'destination':kota_tujuan_id, 'weight':berat_gram, 'courier':self.DEFAULT_COURIER})

        result = req.json()

        ongkir = result['rajaongkir']['results'][0]['costs'][1]['cost'][0]['value']

        # Payment.ongkir = ongkir
        return ongkir

    # Post
    @jwt_required
    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument('cart_id', type=int, location='json')
        parser.add_argument('nama_jalan', location='json', default='None')
        parser.add_argument('rt_rw', location='json', default='None')
        parser.add_argument('kelurahan', location='json', default='None')
        parser.add_argument('kecamatan', location='json', default='None')
        parser.add_argument('kota_kabupaten', location='json', required=True)
        parser.add_argument('provinsi', location='json', default='None')
        parser.add_argument('kode_pos', location='json', default='None')
        parser.add_argument('nomor_telepon', location='json', default='None')
        args = parser.parse_args()

        destinasi = args['kota_kabupaten']

        qry = Cart.query.all()
        berat_kg = 0
        for query in qry:
            if query.status_cart == 1:
                total = berat_kg + query.berat*query.stok
                berat_kg = total
        
        berat_gram = berat_kg*1000
        ongkir_user = self.GetBiayaPengiriman('Malang', destinasi, berat_gram)

        payment = Payment(args['cart_id'],args['nama_jalan'], args['rt_rw'], args['kelurahan'], args['kecamatan'], destinasi, args['provinsi'], args['kode_pos'], args['nomor_telepon'], ongkir_user)

        db.session.add(payment)
        db.session.commit()

        app.logger.debug('DEBUG : %s', payment)
        return ongkir_user, 200, {'Content-Type' : 'application/json'}

class TotalBiaya(Resource):
    def get(self):
        qry = Cart.query.all()
        total_harga = 0
        for query in qry:
            if query.status_cart == 1:
                total = total_harga + query.harga*query.stok
                total_harga = total
        
        qry = Payment.query[-1]
        biaya_ongkir = qry.ongkir

        total_biaya_user = total_harga + biaya_ongkir

        return total_biaya_user

    def post(self):
        qry = Cart.query.all()
        total_harga = 0
        for query in qry:
            if query.status_cart == 1:
                total = total_harga + query.harga*query.stok
                total_harga = total
        
        qry = Payment.query[-1]
        biaya_ongkir = qry.ongkir

        total_biaya_user = total_harga + biaya_ongkir

        return total_biaya_user

api.add_resource(Expedition, '/ongkir')
api.add_resource(TotalBiaya, '/totalbayar')
