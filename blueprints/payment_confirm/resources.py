from mailjet_rest import Client
import os

# Import
from flask import Blueprint
from flask_restful import Api, reqparse, Resource, marshal, inputs
from datetime import datetime
from sqlalchemy import desc
from .model import PaymentConfirm
from blueprints import db, app
from datetime import datetime
from blueprints.user.model import User
from blueprints.cart.model import Cart
from blueprints.book.model import Books
from blueprints.payment.model import Payment
import json
import requests

# Import Authentication
from flask_jwt_extended import jwt_required, get_jwt_claims
from blueprints import internal_required

# To encrypt
from password_strength import PasswordPolicy
import hashlib

# Create blueprint
bp_payment_confirm = Blueprint('payment_confirm', __name__)
api = Api(bp_payment_confirm)

class TotalBiaya(Resource):
    """
    'self' is a variable that represents a function in a class so that the function can be reused in the same class.
    """
    def options(self, id=None):
        """
        To control errors caused by CORS
        """
        return {'status':'ok'},200

    MAILJET_API_KEY = '65c4b0e54802eadb7ff21baa5058ddfa'
    MAILJET_SECRET_KEY = 'c8f9b62ee7246a4278c5a896a2e9c0fd'
    MAILJET_SEND_API = 'https://api.mailjet.com/v3/send'

    @jwt_required
    def post(self):
        """
        Method: GET
        To input a transaction data into the database
        ______________
        
        Parameter Input
        _______________

        Cart: query of carts,
            Cart are objects that exist in the cart table.
        """
        qry = Cart.query.all()
        book_qry = Books.query.all()
        list_barang = []
        claim = get_jwt_claims()
        for query in qry:
            if claim['email'] == query.email and query.status_cart is False:
                list_barang.append(query)
        # Retrieve the order code from the last active cart ID
        kode_pemesanan = hashlib.md5(str(qry[-1].id).encode()).hexdigest()[-10:].upper()

        email = ''
        emailuser = ''

        total_harga = 0
        for query in list_barang:
            if query.status_cart == 0:
                total = total_harga + query.harga*query.stok
                total_harga = total
                for book in book_qry:
                    if book.status == 'Ready Stock':
                        if query.book_id == book.id:
                            remaining = book.stok - query.stok
                            book.stok = remaining
                            db.session.commit()
                email = query.email
                emailuser = query.email
                # Change the cart status to 'paid'
                query.status_cart = True
                db.session.commit()

        qry = Payment.query[-1]
        biaya_ongkir = qry.ongkir

        total_biaya_user = total_harga + biaya_ongkir

        # Send an email containing the payment receipt to the user's email
        mailjet = Client(auth=(self.MAILJET_API_KEY, self.MAILJET_SECRET_KEY), version='v3')
        data = {
                'FromEmail': "lian@alterra.id",
                'FromName': "Kutu Buku",
                'Recipients': [
                        {
                        "Email": "{}".format(email),
                        "Name": "{}".format(emailuser)
                        }
                    ],
                'Subject': "Konfirmasi Pembayaran",
                'Text-part': "Silakan Lakukan Pembayaran Anda!",
                'Html-part': "<h3>Silakan Lakukan Pembayaran Anda!</h3><br />Total Pembayaran = Rp. {}<br />Dengan Kode Pemesanan = {}".format(total_biaya_user, kode_pemesanan)
                }
        result = mailjet.send.create(data=data)

        payment_confirm = PaymentConfirm(total_biaya_user, kode_pemesanan)

        db.session.add(payment_confirm)
        db.session.commit()

        app.logger.debug('DEBUG : %s', payment_confirm)
        
        return marshal(payment_confirm, PaymentConfirm.payment_confirm_fields), 200, {'Content-Type' : 'application/json'}

class SemuaTransaksi(Resource):
    """
    'self' is a variable that represents a function in a class so that the function can be reused in the same class.
    """
    def options(self, id=None):
        """
        To control errors caused by CORS
        """
        return {'status':'ok'},200
    @jwt_required
    def get(self):
        """
        Method: GET
        To retrieve all existing transaction data.
        ______________
        
        Parameter Input
        _______________
        
        PaymentConfirm: query of payment confirmations,
            PaymentConfirm are objects that exist in the payment confirmation   
            table.
        """
        qry = PaymentConfirm.query.all()
        filter_result = []
        for query in qry:
            filter_result.append(marshal(query, PaymentConfirm.payment_confirm_fields))
        return filter_result

class KodePemesanan(Resource):
    """
    'self' is a variable that represents a function in a class so that the function can be reused in the same class.
    """
    def options(self, id=None):
        """
        To control errors caused by CORS
        """
        return {'status':'ok'},200
    def get(self):
        """
        Method: GET
        Order Number and Order Date Search
        ______________
        
        Parameter Input
        _______________

        p: integer (not required),
            p is the index number of the page that the user wants to display.
        rp: integer (not required),
            rp is the number of outputs that will be displayed on one page.
        PaymentConfirm: query of payment confirmations,
            PaymentConfirm are objects that exist in the payment confirmation   
            table.
        keyword: string (not required),
            A keyword is a group of characters entered by a user. Search by order number or order date
        """
        parser = reqparse.RequestParser()
        parser.add_argument('p', location='args', default=1)
        parser.add_argument('rp', location='args', default=25)
        parser.add_argument('keyword', location='args', default='None')
        args = parser.parse_args()

        qry = PaymentConfirm.query
        
        # Search by order number or order date
        if qry:
            search_result = qry.filter(PaymentConfirm.nomor_pemesanan.like('%' + args['keyword'] + '%') | PaymentConfirm.tanggal_pemesanan.like('%' + args['keyword'] + '%'))  
            all_search = []
            for result in search_result:
                all_search.append(marshal(result, PaymentConfirm.payment_confirm_fields))
            return all_search, 200
        return {'status': 'NOT FOUND'}, 404

api.add_resource(TotalBiaya, '/bill')
api.add_resource(SemuaTransaksi, '/all')
api.add_resource(KodePemesanan, '/code')
