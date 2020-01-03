# Import
from flask import Blueprint
from flask_restful import Api, Resource, reqparse, marshal

from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, get_jwt_claims
from flask_jwt_extended import JWTManager, verify_jwt_in_request, get_jwt_claims
from ..user.model import User

# kata_sandi Encription
from password_strength import PasswordPolicy
import hashlib

bp_auth = Blueprint('auth', __name__)
api = Api(bp_auth)

# Resource
class CreateTokenResource(Resource):
    def get(self):
        # Create Token
        parser = reqparse.RequestParser()
        parser.add_argument('email', location='args', required=True)
        parser.add_argument('kata_sandi', location='args', required=True)
        args = parser.parse_args()

        # Internal Client
        if args['email'] == 'lian@alterra.id' and args['kata_sandi'] == 'l3l11234':
            token = create_access_token(identity = args['email'], user_claims={'email': args['email']})
            return {'token': token}, 200

        # Non-Internal User
        else:
            kata_sandi_digest = hashlib.md5(args['kata_sandi'].encode()).hexdigest()
            qry = User.query.filter_by(email = args['email']).filter_by(kata_sandi = kata_sandi_digest)
            userData = qry.first()
            if userData is not None:
                userData = marshal(userData, User.jwt_claim_fields)
                token = create_access_token(identity = args['email'], user_claims=userData)
                return {'token': token}, 200
            return {'status': 'BAD REQUEST', 'message': 'invalid email or kata_sandi'}, 400

    # Show the payload
    @jwt_required
    def post(self):
        verify_jwt_in_request()
        claims = get_jwt_claims()
        claims = marshal(claims, User.jwt_claim_fields)
        return claims, 200
        
api.add_resource(CreateTokenResource, '')