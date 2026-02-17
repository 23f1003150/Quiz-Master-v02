from flask_restful import Resource
from flask import request, jsonify, make_response
from flask_security import utils, auth_token_required , roles_required, login_user


from controllers.user_datastore import user_datastore
from controllers.database import db

#Internally, flask_security_too uses tools like werkzeug.security and passlib for hashing

class CheckEmailAPI(Resource):
    def post(self):
        crediential = request.get_json()

        if not crediential:
            result = {
                'message': 'Request body is required.'
            }
            return make_response(jsonify(result), 400)
        
        email = crediential.get('email', None)

        if not email:
            result = {
                'message': 'Email is required.'
            }
            return make_response(jsonify(result), 400)
        
        user = user_datastore.find_user(email=email)
        if user:
            return make_response(jsonify({'available': False}), 200)
        else:
            return make_response(jsonify({'available': True}), 200)



class LoginAPI(Resource):
    def post(self):
        login_credentials = request.get_json()

        if not login_credentials:
            return make_response(jsonify({'message': 'Login details are required.'}), 400)

        email = login_credentials.get('email')
        password = login_credentials.get('password')

        if not email or not password:
            return make_response(jsonify({'message': 'Email and password are required.'}), 400)

        user = user_datastore.find_user(email=email)

        if not user:
            return make_response(jsonify({'message': 'User not found.'}), 404)

        if not utils.verify_password(password, user.password):
            return make_response(jsonify({'message': 'Invalid password.'}), 401)

        # Login and generate token
        login_user(user)
        token = user.get_auth_token()

        response = {
            'message': '! Login successful to Quiz master !',
            'user_details': {
                'email': user.email,
                'roles': [role.name for role in user.roles],
                'auth_token': token
            }
        }

        return make_response(jsonify(response), 200)


class LogoutAPI(Resource):
    @auth_token_required
    # @roles_required(['admin'])
    def post(self):
        utils.logout_user()
        response = {
            'message': 'Thanks! Logout successful.'
        }
        return make_response(jsonify(response), 200)
    

class RegisterAPI(Resource):
    def post(self):
        creds = request.get_json()

        if not creds:
            result = {
                'message': 'Registration credentials are required.'
            }
            return make_response(jsonify(result), 400)
        
        email = creds.get('email', None)
        password = creds.get('password', None)
        name=creds.get('name',None)

        if not email or not password:
            result = {
                'message': 'Email and password are required.'
            }
            return make_response(jsonify(result), 400)
        
        # if '@' not in email or '.' not in email.split('@')[-1]:
        #     result = {
        #         'message': 'Invalid email format.'
        #     }
        #     return make_response(jsonify(result), 400)
        
        if user_datastore.find_user(email=email):
            result = {
                'message': 'User already exists.'
            }
            return make_response(jsonify(result), 409)
        
        user_role = user_datastore.find_role('user')

        user_datastore.create_user(
            email=email,
            password=password,
            #password = utils.hash_password(password),
            name=name,
            roles = [user_role]
        )

        db.session.commit()

        response = {
            'message': 'Registration successful.',
            'user_details': {
                'email': email,
                'name':name,
                'roles': [user_role.name]
            }
        }
        return make_response(jsonify(response), 201)