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

# Untuk melakukan enkripsi
from password_strength import PasswordPolicy
import hashlib

# Membuat blueprint
bp_payment_confirm = Blueprint('payment_confirm', __name__)
api = Api(bp_payment_confirm)

class TotalBiaya(Resource):
    def options(self, id=None):
        return {'status':'ok'},200

    MAILJET_API_KEY = '65c4b0e54802eadb7ff21baa5058ddfa'
    MAILJET_SECRET_KEY = 'c8f9b62ee7246a4278c5a896a2e9c0fd'
    MAILJET_SEND_API = 'https://api.mailjet.com/v3/send'

    # Triger menekan tombol 'Bayar Sekarang' untuk menuju halaman terakhir
    @jwt_required
    def post(self):
        qry = Cart.query.all()
        book_qry = Books.query.all()
        list_barang = []
        claim = get_jwt_claims()
        for query in qry:
            if claim['email'] == query.email and query.status_cart is False:
                list_barang.append(query)
        # Mengambil kode pemesanan dari ID cart terakhir yang aktif
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
                # Mengubah status cart menjadi 'sudah dibayar'
                query.status_cart = True
                db.session.commit()
        
        qry = Payment.query[-1]
        biaya_ongkir = qry.ongkir

        total_biaya_user = total_harga + biaya_ongkir

        # Mengirim email berisi resi pembayaran ke email user
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
                'Html-part': "<h3>Silakan Lakukan Pembayaran Anda!</h3><br />Total Pembayaran = {}<br />Dengan Kode Pemesanan = {}".format(total_biaya_user, kode_pemesanan)
                }
        result = mailjet.send.create(data=data)

        payment_confirm = PaymentConfirm(total_biaya_user, kode_pemesanan)

        db.session.add(payment_confirm)
        db.session.commit()

        app.logger.debug('DEBUG : %s', payment_confirm)
        
        return marshal(payment_confirm, PaymentConfirm.payment_confirm_fields), 200, {'Content-Type' : 'application/json'}

api.add_resource(TotalBiaya, '/bill')
