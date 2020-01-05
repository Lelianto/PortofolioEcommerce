# Import
from blueprints import db
from flask_restful import fields
from blueprints.user.model import User
from blueprints.book.model import Books

# Membuat Model keranjang dengan nama tabel 'cart'
class Cart(db.Model):
    __tablename__ = 'cart'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    status_cart = db.Column(db.Boolean, nullable=False, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    judul = db.Column(db.String(255), nullable=False)
    penulis = db.Column(db.String(255), nullable=False)
    jenis_cover = db.Column(db.String(255), nullable=False)
    foto_buku = db.Column(db.String(255), nullable=False)
    harga = db.Column(db.Integer, nullable=False)
    stok = db.Column(db.Integer, nullable=False)
    berat = db.Column(db.Float, nullable=False)
    nama_lengkap = db.Column(db.String(255), nullable = False)
    email = db.Column(db.String(255), nullable = False)
    
    cart_fields = {
        'id': fields.Integer,
        'status_cart' : fields.Boolean,
        'user_id' : fields.Integer,
        'book_id' : fields.Integer,
        'judul' : fields.String,
        'penulis' : fields.String,
        'jenis_cover' : fields.String,
        'foto_buku' : fields.String,
        'harga' : fields.Integer,
        'stok' : fields.Integer,
        'berat' : fields.Integer,
        'nama_lengkap' : fields.String,
        'email' : fields.String
    }

# Melakukan inisiasi variabel yang akan digunakan di resource
    def __init__(self, status_cart, user_id, book_id, judul, penulis, jenis_cover, foto_buku, harga, stok, berat, nama_lengkap, email):
        self.status_cart = status_cart
        self.user_id = user_id
        self.book_id = book_id
        self.judul = judul
        self.penulis = penulis
        self.jenis_cover = jenis_cover
        self.foto_buku = foto_buku
        self.harga = harga
        self.stok = stok
        self.berat = berat
        self.nama_lengkap = nama_lengkap
        self.email = email

    def __repr__(self):
        return '<Cart %r>' % self.id