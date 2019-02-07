from flask import Flask;
from flask_sqlalchemy import SQLAlchemy;

import Config;

db = SQLAlchemy();

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config); #导入config.py文件中的配置
    db.init_app(app)    #避免循环引用
    return app