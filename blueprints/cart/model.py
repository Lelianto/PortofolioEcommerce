# Import
from blueprints import db
from flask_restful import fields
from blueprints.user.model import User
from blueprints.book.model import Books

# Create Model
class Cart(db.Model):
    __tablename__ = 'cart'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    total_beli = db.Column(db.Integer, nullable=False, default=0)
    total_harga = db.Column(db.Integer, nullable=False, default=0)
    status_cart = db.Column(db.Boolean, nullable=False, default=False)

    judul = db.Column(db.String(255), nullable=False)
    penulis = db.Column(db.String(255), nullable=False)
    jenis_cover = db.Column(db.String(255), nullable=False)
    foto_buku = db.Column(db.String(255), nullable=False)
    harga = db.Column(db.Integer, nullable=False)
    stok = db.Column(db.Integer, nullable=False)

    nama_lengkap = db.Column(db.String(255), nullable = False)
    email = db.Column(db.String(255), unique= True, nullable = False)
    
    cart_fields = {
        'id': fields.Integer,
        'user_id' : fields.Integer,
        'book_id' : fields.Integer,
        'total_beli' : fields.Integer,
        'total_harga' : fields.Integer,
        'status_cart' : fields.Boolean,
        'judul' : fields.String,
        'penulis' : fields.String,
        'jenis_cover' : fields.String,
        'foto_buku' : fields.String,
        'harga' : fields.Integer,
        'stok' : fields.Integer,
        'nama_lengkap' : fields.String,
        'email' : fields.String
    }

    def __init__(self, user_id, book_id, total_beli, total_harga, status_cart, judul, penulis, jenis_cover, foto_buku, harga, stok, nama_lengkap, email):
        self.user_id = user_id
        self.book_id = book_id
        self.total_beli = total_beli
        self.total_harga = total_harga
        self.status_cart = status_cart
        self.judul = judul
        self.penulis = penulis
        self.jenis_cover = jenis_cover
        self.foto_buku = foto_buku
        self.harga = harga
        self.stok = stok
        self.nama_lengkap = nama_lengkap
        self.email = email

    # def __repr__(self):
    #     return '<Cart %r>' % self.id