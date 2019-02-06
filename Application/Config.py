#dialect+driver://username:password@host:port/database

DIALECT='mysql';
DRIVER='mysqlconnector';
USERNAME='root';
PASSWORD='m(24Virgo';
HOST='127.0.0.1';
PORT='3306';
DATABASE='flask_db';

SECRET_KEY = '123';
SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE);
SQLALCHEMY_TRACK_MODIFICATIONS = True;

DEBUG = True;