from datetime import datetime 
from blueprints import db 
from flask_restful import fields
from blueprints.user.model import User

class Books(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    judul = db.Column(db.String(255), nullable=False)
    penulis = db.Column(db.String(255), nullable=False)
    jumlah_halaman = db.Column(db.Integer, nullable=False)
    tanggal_terbit = db.Column(db.String(255), nullable=False)
    isbn = db.Column(db.String(50), unique=True, nullable=False)
    genre = db.Column(db.String(255), nullable=False)
    bahasa = db.Column(db.String(255), nullable=False)
    berat = db.Column(db.Float, nullable=False)
    lebar = db.Column(db.Integer, nullable=False)
    panjang = db.Column(db.Integer, nullable=False)
    jenis_cover = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(255), nullable=False)
    foto_buku = db.Column(db.String(255), nullable=False)
    sinopsis = db.Column(db.String(10000), nullable=False)
    harga = db.Column(db.Integer, nullable=False)
    stok = db.Column(db.Integer, nullable=False)

    response_fields = {
        'id' : fields.Integer,
        'user_id' : fields.Integer,
        'judul' : fields.String,
        'penulis' : fields.String,
        'jumlah_halaman' : fields.Integer,
        'tanggal_terbit' : fields.String,
        'isbn' : fields.String,
        'genre' : fields.String,
        'bahasa' : fields.String,
        'berat' : fields.Float,
        'lebar' : fields.Integer,
        'panjang' : fields.Integer,
        'jenis_cover' : fields.String,
        'status' : fields.String,
        'foto_buku' : fields.String,
        'sinopsis' : fields.Integer,
        'harga' : fields.Integer,
        'stok' : fields.Integer
    }

    def __init__(self, user_id, judul, penulis, jumlah_halaman, tanggal_terbit, isbn, genre, bahasa, berat, lebar, panjang, jenis_cover, status, foto_buku, sinopsis, harga, stok):
        self.user_id = user_id
        self.judul = judul
        self.penulis = penulis
        self.jumlah_halaman = jumlah_halaman
        self.tanggal_terbit = tanggal_terbit
        self.isbn = isbn
        self.genre = genre
        self.bahasa = bahasa
        self.berat = berat
        self.lebar = lebar
        self.panjang = panjang
        self.jenis_cover = jenis_cover
        self.status = status
        self.foto_buku = foto_buku
        self.sinopsis = sinopsis
        self.harga = harga
        self.stok = stok

    def __repr__(self):
        return '<Book %r' % self.id