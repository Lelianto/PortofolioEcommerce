# Import
from blueprints import db
from flask_restful import fields

# Create Model
class Payment(db.Model):
    __tablename__ = 'payment'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'))
    nama_jalan = db.Column(db.String(255), nullable=False)
    rt_rw = db.Column(db.String(255), nullable=False)
    kelurahan = db.Column(db.String(255), nullable=False)
    kecamatan = db.Column(db.String(255), nullable=False)
    kota_kabupaten = db.Column(db.String(255), nullable=False)
    provinsi = db.Column(db.String(255), nullable=False)
    kode_pos = db.Column(db.String(255), nullable=False)
    nomor_telepon = db.Column(db.String(255), nullable=False)
    ongkir = db.Column(db.Integer, nullable=False)
 

    payment_fields = {
        'id': fields.Integer,
        'cart_id': fields.Integer,
        'nama_jalan': fields.String,
        'rt_rw': fields.String,
        'kelurahan': fields.String,
        'kecamatan': fields.String,
        'kota_kabupaten': fields.String,
        'provinsi': fields.String,
        'kode_pos': fields.String,
        'nomor_telepon': fields.String,
        'ongkir': fields.Integer
    }

    def __init__(self, cart_id, nama_jalan, rt_rw, kelurahan, kecamatan, kota_kabupaten, provinsi, kode_pos, nomor_telepon, ongkir=0):
        self.cart_id = cart_id,
        self.nama_jalan = nama_jalan,
        self.rt_rw = rt_rw,
        self.kelurahan = kelurahan,
        self.kecamatan = kecamatan,
        self.kota_kabupaten = kota_kabupaten,
        self.provinsi = provinsi,
        self.kode_pos = kode_pos,
        self.nomor_telepon = nomor_telepon
        self.ongkir = ongkir

    def __repr__(self):
        return '<Payment %r>' % self.id