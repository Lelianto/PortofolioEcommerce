# Import library yang dibutuhkan
from flask import Blueprint
from flask_restful import Api, reqparse, Resource, marshal, inputs
from datetime import datetime
from sqlalchemy import desc
from .model import User
from blueprints import db, app
from datetime import datetime
import json
# Import Authentication
from flask_jwt_extended import jwt_required, get_jwt_claims
from blueprints import internal_required
# Untuk melakukan enkripsi
from password_strength import PasswordPolicy
import hashlib

# Membuat blueprint user
bp_user = Blueprint('user', __name__)
api = Api(bp_user)

class UserResource(Resource):
    def options(self, id=None):
        return {'status':'ok'},200
        
    # Untuk menampilkan isi profil user sesuai ID user (hanya miliknya sendiir)
    # Untuk menampilkan seluruh profil pada seluruh ID (jika internal)
    @jwt_required
    def get(self, id):
        qry = User.query.get(id)
        claim = get_jwt_claims()
        if claim['email'] == 'lian@alterra.id':
            return marshal(qry, User.user_fields), 
        else:
            if qry and int(claim['id'] == id):
                return marshal(qry, User.user_fields), 200
            return {'status': 'NOT FOUND'}, 404

    # Melakukan update data pada profil user
    @jwt_required
    def put(self, id):
        if int(id) > 0:
            user = User.query.get(id)
            if user:
                # User dapat mengupdate data sesuai field di bawah ini
                parser = reqparse.RequestParser()
                parser.add_argument('tanggal_lahir', location='args')
                parser.add_argument('nomor_telepon', location='args')
                parser.add_argument('foto_profil', location='args')
                parser.add_argument('genre', location='args')
                args = parser.parse_args()

                # Melakukan update data pada tabel
                user.tanggal_lahir = args['tanggal_lahir']
                user.nomor_telepon = args['nomor_telepon']
                user.foto_profil = args['foto_profil']
                user.genre = args['genre']
                db.session.commit()
                user = marshal(user, User.user_fields)
                app.logger.debug('DEBUG : %s', user)
                    
                return user, 200, {'Content-Type':'application/json'}
            return {'status' : 'NOT FOUND'}, 404, {'Content-Type':'application/json'}
        return {'status' : 'BAD REQUEST'}, 400, {'Content-Type':'application/json'}

    # Menghapus user sesuai ID
    @jwt_required
    def delete(self, id):
        user = User.query.get(id)
        if user is not None:
            # Hard Delete
            claim = get_jwt_claims()
            # Internal dapat menghapus semua user sesuai ID
            if claim['email'] == 'lian@alterra.id':
                db.session.delete(user)
                db.session.commit()
                return {'status': 'DELETED'}, 200, {'Content-Type':'application/json'}
            else:
                # User hanya dapat menghapus dirinya sendiri - pada aplikasi nyata, token akan dihapus dari setiap page
                if user and int(claim['id']) == int(id):
                    db.session.delete(user)
                    db.session.commit()
                    return {'status': 'DELETED'}, 200, {'Content-Type':'application/json'}
                return {'status': 'NOT FOUND'}, 404
        return {'status' : 'There are no user with this ID'}, 404, {'Content-Type':'application/json'}

class UserList(Resource):
    # Menampilkan seluruh user - hanya dapat dilakukan oleh Internal

    def options(self, id=None):
        return {'status':'ok'},200
        
    @jwt_required
    @internal_required
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('p', location='json', default=1)
        parser.add_argument('rp', location='json', default=25)
        args = parser.parse_args()

        # Pagination hasil tampilan user
        offset = args['rp'] * (args['p'] - 1)

        # Menyimpan query User pada sebuah variabel
        qry = User.query
        
        # Menyimpan hasil dalam sebuah list yang berisi object
        filter_result = []
        for query in qry.limit(args['rp']).offset(offset):
            filter_result.append(marshal(query, User.user_fields))
        return filter_result

    # Melakukan pendaftaran user - dapat dilakukan siapapun
    def post(self):
        # Setup the policy
        policy = PasswordPolicy.from_names(
            length = 6
        )

        parser = reqparse.RequestParser()
        parser.add_argument('nama_lengkap', location='json', required=True)
        parser.add_argument('email', location='json', required=True)
        parser.add_argument('kata_sandi', location='json', required=True)
        parser.add_argument('tanggal_lahir', location='json')
        parser.add_argument('nomor_telepon', location='json')
        parser.add_argument('foto_profil', location='json')
        parser.add_argument('genre', location='json')
        args = parser.parse_args()

        validation = policy.test(args['kata_sandi'])

        # Melakukan validasi kata sandi sesuai aturan yang telah dibuat (policy)
        if validation == []:
            kata_sandi_digest = hashlib.md5(args['kata_sandi'].encode()).hexdigest()
            # Membuat object user baru
            user = User(args['nama_lengkap'], args['email'], kata_sandi_digest, args['tanggal_lahir'], args['nomor_telepon'], args['foto_profil'], args['genre'])
            # Menyimpan user ke dalam database
            db.session.add(user)
            db.session.commit()

            app.logger.debug('DEBUG : %s', user)

            return marshal(user, User.user_fields), 200, {'Content-Type':'application/json'}

class UserProfile(Resource):
    def options(self, id=None):
        return {'status':'ok'},200
        
    # Untuk menampilkan isi profil user
    @jwt_required
    def get(self):
        claim = get_jwt_claims()
        result = User.query.get(claim['id'])
        return marshal(result, User.user_fields)

api.add_resource(UserList, '')
api.add_resource(UserProfile,'/profile')
api.add_resource(UserResource, '/<id>')