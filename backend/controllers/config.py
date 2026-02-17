class Config:
    SECRET_KEY='my_sceret_key' # for session management and security
    SQLALCHEMY_DATABASE_URI = 'sqlite:///bankdatabase.db'
   

    
    SECRET_PASSWORD_SALT='some_random_salt' # for password hashing and security
    
    SECURITY_TOKEN_AUTHENTICATION_KEY ='auth_token' # for token-based authentication
    SECURITY_TOKEN_AUTHENTICATION_HEADER= 'Authentication-Token' # header name for token authentication
    
    SECURITY_TOKEN_MAX_AGE = 3600