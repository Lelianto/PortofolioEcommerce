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
    """
    'self' is a variable that represents a function in a class so that the function can be reused in the same class.
    """
    def options(self, id=None):
        """
        To control errors caused by CORS
        """
        return {'status':'ok'},200
        
    @jwt_required
    def get(self, id):
        """
        Method: GET
        Display all users by id - only by internal
        - To display user profile contents according to user ID (only his own)
        - To display the entire profile on all IDs (if internal)
        ______________
        
        Parameter Input
        _______________

        id: params integer (required),
            User provides input id when performing a function execution (input 
            entered into params)
        User: query of user data,
             User are objects that exist in the user table.
        """
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
        """
        Method: PUT
        - Do data updating on user profiles
        ______________
        
        Parameter Input
        _______________

        id: params integer (required),
            User provides input id when performing a function execution (input 
            entered into params)
        tanggal_lahir, nomor_telepon, foto_profil, genre: string (not required)
        """
        if int(id) > 0:
            user = User.query.get(id)
            if user:
                # Users can update the data according to the fields below
                parser = reqparse.RequestParser()
                parser.add_argument('tanggal_lahir', location='args')
                parser.add_argument('nomor_telepon', location='args')
                parser.add_argument('foto_profil', location='args')
                parser.add_argument('genre', location='args')
                args = parser.parse_args()

                # Perform data updates on the table
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
        """
        Method: PUT
        Deleting user according ID (Hard Delete)
        Admin can delete all users according ID
        ______________
        
        Parameter Input
        _______________

        id: params integer (required),
            User provides input id when performing a function execution (input 
            entered into params)
        """
        user = User.query.get(id)
        if user is not None:
            claim = get_jwt_claims()
            # Internal dapat menghapus semua user sesuai ID
            if claim['email'] == 'lian@alterra.id':
                db.session.delete(user)
                db.session.commit()
                return {'status': 'DELETED'}, 200, {'Content-Type':'application/json'}
            else:
                # Users can only delete themselves - in real applications, tokens will be deleted from each page
                if user and int(claim['id']) == int(id):
                    db.session.delete(user)
                    db.session.commit()
                    return {'status': 'DELETED'}, 200, {'Content-Type':'application/json'}
                return {'status': 'NOT FOUND'}, 404
        return {'status' : 'There are no user with this ID'}, 404, {'Content-Type':'application/json'}

class UserList(Resource):
    """
    'self' is a variable that represents a function in a class so that the function can be reused in the same class.
    """
    def options(self, id=None):
        """
        To control errors caused by CORS
        """
        return {'status':'ok'},200
        
    @jwt_required
    @internal_required
    def get(self):
        """
        Method: GET
        Display all users - only by internal
        ______________
        
        Parameter Input
        _______________

        p: integer (not required),
             p is the index number of the page that the user wants to display.
        rp: integer (not required),
             rp is the number of outputs that will be displayed on one page.
        User: query of user data,
             User are objects that exist in the user table.
        """
        parser = reqparse.RequestParser()
        parser.add_argument('p', location='json', default=1)
        parser.add_argument('rp', location='json', default=25)
        args = parser.parse_args()

        # Pagination user display results
        offset = args['rp'] * (args['p'] - 1)

        # Stores a User query on a variable
        qry = User.query
        
        # Stores the results in a list containing objects
        filter_result = []
        for query in qry.limit(args['rp']).offset(offset):
            filter_result.append(marshal(query, User.user_fields))
        return filter_result

    def post(self):
        """
        Method: POST
        User registration - anyone can do it.
        ______________
        
        Parameter Input
        _______________

        nama_lengkap, email, kata_sandi, tanggal_lahir, nomor_telepon, foto_profil, genre: string
            nama_lengkap, email, and kata_sandi is required, the others isn't required
        kata_sandi_digest: *all types (length:6 characters),
             Hide passwords using hashlib
        """
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

        # Validating passwords according to rules that have been made (policy)
        if validation == []:
            kata_sandi_digest = hashlib.md5(args['kata_sandi'].encode()).hexdigest()
            # Create a new user object
            user = User(args['nama_lengkap'], args['email'], kata_sandi_digest, args['tanggal_lahir'], args['nomor_telepon'], args['foto_profil'], args['genre'])
            # Save the user to the database
            db.session.add(user)
            db.session.commit()

            app.logger.debug('DEBUG : %s', user)

            return marshal(user, User.user_fields), 200, {'Content-Type':'application/json'}

class UserProfile(Resource):
    """
    'self' is a variable that represents a function in a class so that the function can be reused in the same class.
    """
    def options(self, id=None):
        """
        To control errors caused by CORS
        """
        return {'status':'ok'},200
        
    # Untuk menampilkan isi profil user
    @jwt_required
    def get(self):
        """
        Method: GET
        Display all users by id - by user itself
        - To display user profile contents according to user ID (only his own)
        ______________
        
        Parameter Input
        _______________

        id: params integer (required),
            User provides input id when performing a function execution (input 
            entered into params)
        User: query of user data,
             User are objects that exist in the user table.
        """
        claim = get_jwt_claims()
        result = User.query.get(claim['id'])
        return marshal(result, User.user_fields)

api.add_resource(UserList, '')
api.add_resource(UserProfile,'/profile')
api.add_resource(UserResource, '/<id>')