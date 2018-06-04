from flaskApp import *;
from flask import session,request;
from datetime import timedelta;
from Model import *;

appIns = create_app();

# session.permanent = True;
# appIns.permanent_session_lifetime = timedelta(minutes=5);
with appIns.app_context():
    db.create_all();


@appIns.route('/',methods =['GET','POST'])
def Home():
    #增
    # article1 = Article(title = '321', content = 'fuck you!');  #一个对象就是一条数据
    # db.session.add(article1);  #加入进数据库
    # db.session.commit(); #提交

    #查
    # article = Article.query.filter(Article.title == '321').first();

    #改 = 查出来改了再提交

    #删 = 查出来删了再提交
    # article = Article.query.filter(Article.id == 1).first();
    # if article:
    #     db.session.delete(article);
    #     db.session.commit();
    # user1 = User(username='tangyao');
    # db.session.add(user1);
    # db.session.commit();

    # user = TestTable(content = 'content000');
    # db.session.add(user);
    # db.session.commit();
    # user = TestTable1(content='content001');
    # db.session.add(user);
    # db.session.commit();

    # session['username'] = 'Tangyao'


    # return render_template('Test.html',title='首页');
    return render_template('Main.html',title='首页');

if __name__ == "__main__":
    appIns.run(debug=True);

