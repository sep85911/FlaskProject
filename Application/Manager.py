from flask_script import Manager; #在控制台操作flask
from flask_migrate import Migrate, MigrateCommand; #数据迁移 数据库字段改变后使用 create_all只会调用一次
from Main import appIns;
from flaskApp import db;

# import Main;

DBM = Manager(appIns);

migrate = Migrate(appIns,db);

DBM.add_command('db',MigrateCommand);

# @DBM.command
# def Init():
#     appIns.run(debug = True);
#     print('我艹！这都能初始化呀？');

if __name__ == '__main__':
    DBM.run();
