# Import beberapa library yang dibutuhkan
from flask import Blueprint
from flask_restful import Api, Resource, reqparse, marshal
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, get_jwt_claims
from flask_jwt_extended import JWTManager, verify_jwt_in_request, get_jwt_claims
from ..user.model import User
# Untuk melakukan enkripsi
from password_strength import PasswordPolicy
import hashlib

bp_auth = Blueprint('auth', __name__)
api = Api(bp_auth)

# Resource class untuk membuat token
class CreateTokenResource(Resource):
    def options(self, id=None):
        return {'status':'ok'},200

    def post(self):
        """
        Parameter Input
        _______________

        email: string,
            user atau admin menginput data email (sudah pasti unik)
        kata_sandi: string,
            user menginput kata sandi sesuai dengan input yang bersyarat pada bagian 
        """
        # Untuk melakukan login dan pengecekan tipe akun 
        parser = reqparse.RequestParser()
        parser.add_argument('email', location='json', required=True)
        parser.add_argument('kata_sandi', location='json', required=True)
        args = parser.parse_args()

        # Pengecekan : Apakah termasuk akun internal
        if args['email'] == 'lian@alterra.id' and args['kata_sandi'] == 'l3l11234':
            token = create_access_token(identity = args['email'], user_claims={'email': args['email']})
            return {'token': token}, 200

        # Logika yang berjalan jika ternyata yang login adalah user biasa
        else:
            kata_sandi_digest = hashlib.md5(args['kata_sandi'].encode()).hexdigest()
            qry = User.query.filter_by(email = args['email']).filter_by(kata_sandi = kata_sandi_digest)
            userData = qry.first()
            if userData is not None:
                userData = marshal(userData, User.jwt_claim_fields)
                token = create_access_token(identity = args['email'], user_claims=userData)
                return {'token': token}, 200
            return {'status': 'BAD REQUEST', 'message': 'invalid email or kata_sandi'}, 400

# Endpoint untuk login
api.add_resource(CreateTokenResource, '')