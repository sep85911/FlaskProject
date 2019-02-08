from flask import Flask;


from app.main import Extensions;
from app.main import Views;

import Config;

def create_app():
    app = Flask(__name__,template_folder="../templates")
    app.register_blueprint(Views.bp)
    app.config.from_object(Config); #导入config.py文件中的配置

    
    Extensions.db.init_app(app)    #避免循环引用
    return app


