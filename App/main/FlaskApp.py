from flask import Flask;

from App.main import Views as MainViews; # 导入app/main下面的视图函数py文件
from .Extensions import db;
import Config;

def RegisterBP(appIns):
    appIns.register_blueprint(MainViews.bp);

def CreateApp():

    # 初始化Flask实例
    app = Flask(__name__,template_folder="../templates",static_folder="../static");

    # 注册蓝图
    RegisterBP(app);

    # 导入配置
    app.config.from_object(Config);

    # 初始化数据库
    db.init_app(app);

    db.create_all(app=app);

    return app;