import os
from datetime import timedelta


class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TEMPLATES_AUTO_RELOAD = True
    SEVER_NAME = '0.0.0.0'
    PREFERRED_URL_SCHEME = 'https'
    UPLOADED_PHOTOS_DEST = "App/uploads"
    JWT_TOKEN_LOCATION = ["headers"]


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=int(os.environ.get('JWT_ACCESS_TOKEN_EXPIRES', 10)))
    ENV = "PRODUCTION"


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SECRET_KEY = "hg0xuE8Ryo0zKWNPViNUe5PxBr6DgKCsjWn0cPb8avYy2aYX_cp2_FO_j_WPMP_6oKIjh_sf9yW8Yl1EpkqraA"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=10)
    ENV = "DEVELOPMENT"


config = {
    'PRODUCTION': ProductionConfig(),
    'DEVELOPMENT': DevelopmentConfig(),
    'DEFAULT': DevelopmentConfig()
}


def load_config():
    return config[os.environ.get('ENV', 'DEFAULT')]

# import os
# import importlib
# from datetime import timedelta
#
# # must be updated to inlude addtional secrets/ api keys & use a gitignored custom-config file instad
# def load_config():
#     config = {'ENV': os.environ.get('ENV', 'DEVELOPMENT')}
#     delta = 7
#     if config['ENV'] == "DEVELOPMENT":
#         from .default_config import JWT_ACCESS_TOKEN_EXPIRES, SQLALCHEMY_DATABASE_URI, SECRET_KEY
#         config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
#         config['SECRET_KEY'] = SECRET_KEY
#         delta = JWT_ACCESS_TOKEN_EXPIRES
#     else:
#         config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
#         config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
#         config['RAWG_TOKEN'] = os.environ.get('RAWG_TOKEN')
#         config['DEBUG'] = config['ENV'].upper() != 'PRODUCTION'
#         delta = int(os.environ.get('JWT_ACCESS_TOKEN_EXPIRES', 7))
#
#     config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=int(delta))
#     config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     config['TEMPLATES_AUTO_RELOAD'] = True
#     config['SEVER_NAME'] = '0.0.0.0'
#     config['PREFERRED_URL_SCHEME'] = 'https'
#     config['UPLOADED_PHOTOS_DEST'] = "App/uploads"
#     config["JWT_TOKEN_LOCATION"] = ["headers"]
#     return config
#
# config = load_config()
