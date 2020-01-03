# Import
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

# kata_sandi Encription
from password_strength import PasswordPolicy
import hashlib

# Creating blueprint
bp_user = Blueprint('user', __name__)
api = Api(bp_user)

class UserResource(Resource):
    # Get By ID
    @jwt_required
    def get(self, id):
        qry = User.query.get(id)
        claim = get_jwt_claims()
        if claim['email'] == 'lian@alterra.id':
            return marshal(qry, User.user_fields), 
        else:
            if qry and claim['id'] == id:
                return marshal(qry, User.user_fields), 200
            return {'status': 'NOT FOUND'}, 404

    # Put
    @jwt_required
    def put(self, id):
        # validasi id gak ngaco
        if int(id) > 0:
            user = User.query.get(id)
            if user:
                parser = reqparse.RequestParser()
                parser.add_argument('tanggal_lahir', location='args')
                parser.add_argument('nomor_telepon', location='args')
                parser.add_argument('foto_profil', location='args')
                parser.add_argument('genre', location='args')
                args = parser.parse_args()

                # Updated the object
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

    # Delete
    @jwt_required
    def delete(self, id):
        user = User.query.get(id)

        if user is not None:
            # Hard Delete
            db.session.delete(user)
            db.session.commit()
            return {'status': 'DELETED'}, 200, {'Content-Type':'application/json'}
        return {'status' : 'NOT FOUND'}, 404, {'Content-Type':'application/json'}

class UserList(Resource):
    # Get All
    @jwt_required
    @internal_required
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('p', location='args', default=1)
        parser.add_argument('rp', location='args', default=25)
        args = parser.parse_args()

        # Pagination
        offset = args['rp'] * (args['p'] - 1)

        # Querying all rows of Client Table
        qry = User.query
        
        # Store the result in a list and return
        filter_result = []
        for query in qry.limit(args['rp']).offset(offset):
            filter_result.append(marshal(query, User.user_fields))
        return filter_result

    # Post
    def post(self):
        # Setup the policy
        policy = PasswordPolicy.from_names(
            length = 6
        )

        parser = reqparse.RequestParser()
        parser.add_argument('nama_lengkap', location='args', required=True)
        parser.add_argument('email', location='args', required=True)
        parser.add_argument('kata_sandi', location='args', required=True)
        parser.add_argument('tanggal_lahir', location='args')
        parser.add_argument('nomor_telepon', location='args')
        parser.add_argument('foto_profil', location='args')
        parser.add_argument('genre', location='args')
        args = parser.parse_args()

        validation = policy.test(args['kata_sandi'])

        if validation == []:
            kata_sandi_digest = hashlib.md5(args['kata_sandi'].encode()).hexdigest()
            # Creating object
            user = User(args['nama_lengkap'], args['email'], kata_sandi_digest, args['tanggal_lahir'], args['nomor_telepon'], args['foto_profil'], args['genre'])
            db.session.add(user)
            db.session.commit()

            app.logger.debug('DEBUG : %s', user)

            return marshal(user, User.user_fields), 200, {'Content-Type':'application/json'}

api.add_resource(UserList, '')
api.add_resource(UserResource, '/<id>')