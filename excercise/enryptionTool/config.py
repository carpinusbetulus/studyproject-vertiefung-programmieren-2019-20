"""Flask config class"""


# in the real world the configuration should be stored in a .env file,
# but because it should work with our settings on differnt computers. It is stored here.
# Se more here: https://hackersandslackers.com/configure-flask-applications
class Config:
    """Sets Flask configuartion variables"""
    Testing = True
    DEBUG = True
    SECRET_KEY = b'ayTAyD2feEGDS6P9eZwj'

    # Database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database/datalog.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False