from flask import Flask
from flask_security import Security
from flask_restful import Api
from flask_cors import CORS # Cross-Origin Resource Sharing

from controllers.database import db
from controllers.user_datastore import user_datastore
from controllers.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    security = Security(app, user_datastore)

    api = Api(app, prefix='/api')

    with app.app_context():
        db.create_all()

        admin_role = user_datastore.find_or_create_role(name='admin', description='Quiz master')
        instructor_role = user_datastore.find_or_create_role(name='instructor', description='Instructors')
        user_role = user_datastore.find_or_create_role(name='user', description='Students')

        if not user_datastore.find_user(email='admin@gmail.com'):
            user_datastore.create_user(
                email = "admin@gmail.com",
                password = "admin123",
                name= "Admin User",
                #password=hash_password("admin123"),
                roles=[admin_role]
            )
        
        if not user_datastore.find_user(email="instructor@gmail.com"):
            user_datastore.create_user(
                email="instructor@gmail.com",
                password="instructor123",
                name="Instructor User",
                roles=[instructor_role]
            )
        
        if not user_datastore.find_user(email='user0@gmail.com'):
            user_datastore.create_user(
                email='user0@gmail.com',
                #password=hash_password("12345"),
                password="12345",
                roles=[user_role]
            )
        
        db.session.commit()

    return app, api


app, api = create_app()
#CORS configuration to allow requests from the frontend(below url only)
CORS(app, origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ])


@app.route('/')
def index():
    return {
        'message': 'Welcome to the Flask Security API!'
    }, 200
    
from controllers.auth_apis import LoginAPI, LogoutAPI, RegisterAPI, CheckEmailAPI
api.add_resource(LoginAPI, '/login')
api.add_resource(LogoutAPI, '/logout')
api.add_resource(RegisterAPI, '/register')
api.add_resource(CheckEmailAPI, '/check-email')

if __name__ == "__main__":
    app.run(debug=True)
