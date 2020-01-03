# Import
from blueprints import db
from flask_restful import fields

# Create Model
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nama_lengkap = db.Column(db.String(255), nullable = False)
    email = db.Column(db.String(255), unique= True, nullable = False)
    kata_sandi = db.Column(db.String(255), nullable = False)
    tanggal_lahir =  db.Column(db.String(10))
    nomor_telepon = db.Column(db.String(15))
    foto_profil = db.Column(db.String(500))
    genre = db.Column(db.String(1000))

    user_fields = {
        'id': fields.Integer,
        'nama_lengkap': fields.String,
        'email': fields.String,
        'kata_sandi': fields.String,
        'tanggal_lahir' : fields.String,
        'nomor_telepon' : fields.String,
        'foto_profil' : fields.String,
        'genre' : fields.String
    }

    jwt_claim_fields = {
        'id' : fields.String,
        'email': fields.String
    }

    def __init__(self, nama_lengkap, email, kata_sandi, tanggal_lahir, nomor_telepon, foto_profil, genre):
        self.nama_lengkap = nama_lengkap
        self.email = email
        self.kata_sandi = kata_sandi
        self.tanggal_lahir = tanggal_lahir
        self.nomor_telepon = nomor_telepon
        self.foto_profil = foto_profil
        self.genre = genre

    def __repr__(self):
        return '<User %r>' % self.id