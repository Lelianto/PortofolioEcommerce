# Import beberapa library yang dibutuhkan
from flask import Blueprint
from flask_restful import Api, Resource, reqparse, marshal
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, get_jwt_claims
from flask_jwt_extended import JWTManager, verify_jwt_in_request, get_jwt_claims
from ..user.model import User
from password_strength import PasswordPolicy
import hashlib

bp_auth = Blueprint('auth', __name__)
api = Api(bp_auth)

# Resource class for creating tokens
class CreateTokenResource(Resource):
    """
    'self' is a variable that represents a function in a class so that the function can be reused in the same class.
    """
    def options(self, id=None):
        """
        To control errors caused by CORS
        """
        return {'status':'ok'},200

    def post(self):
        """
        Method: POST
        ______________
        
        Parameter Input
        _______________

        email: string,
            user or admin input email data (it is definitely unique)
        kata_sandi: string,
            The user inputs the password according to the conditional input in the password section. token will be generated using hashlib syntax
        """
        # To log in and check account types
        parser = reqparse.RequestParser()
        parser.add_argument('email', location='json', required=True)
        parser.add_argument('kata_sandi', location='json', required=True)
        args = parser.parse_args()

        # Checking: Does it include an internal account
        if args['email'] == 'lian@alterra.id' and args['kata_sandi'] == 'l3l11234':
            token = create_access_token(identity = args['email'], user_claims={'email': args['email']})
            return {'token': token}, 200

        # The logic that runs if it turns out that the login is a normal user
        else:
            kata_sandi_digest = hashlib.md5(args['kata_sandi'].encode()).hexdigest()
            qry = User.query.filter_by(email = args['email']).filter_by(kata_sandi = kata_sandi_digest)
            userData = qry.first()
            if userData is not None:
                userData = marshal(userData, User.jwt_claim_fields)
                token = create_access_token(identity = args['email'], user_claims=userData)
                return {'token': token}, 200
            return {'status': 'BAD REQUEST', 'message': 'invalid email or kata_sandi'}, 400

api.add_resource(CreateTokenResource, '')