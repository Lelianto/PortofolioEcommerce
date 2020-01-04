# Import
from blueprints import db
from flask_restful import fields
from datetime import datetime

# Create Model
class PaymentConfirm(db.Model):
    __tablename__ = 'payment_confirm'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    total_biaya = db.Column(db.Integer, nullable=False)
    nomor_pemesanan = db.Column(db.String(255), nullable=False)
    tanggal_pemesanan = db.Column(db.String(255), nullable=False,
        default=datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))
 
    payment_confirm_fields = {
        'id': fields.Integer,
        'total_biaya': fields.Integer,
        'nomor_pemesanan': fields.String,
        'tanggal_pemesanan': fields.String
    }

    def __init__(self, total_biaya, nomor_pemesanan):
        self.total_biaya = total_biaya,
        self.nomor_pemesanan = nomor_pemesanan
        self.tanggal_pemesanan = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

    def __repr__(self):
        return '<PaymentConfirm %r>' % self.id