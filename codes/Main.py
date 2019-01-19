from flaskApp import *;
from flask import session,request,url_for,redirect,render_template;
from datetime import timedelta;
from Model import *;

# appIns = create_app();

# session.permanent = True;
# appIns.permanent_session_lifetime = timedelta(minutes=5);
# with appIns.app_context():
#     db.create_all();


# @appIns.route('/',methods =['GET','POST'])
# def Home():
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


    # # return render_template('Test.html',title='首页');
    # return render_template('home.html',title='首页');

# @appIns.route('/login/', methods=['GET','POST'])
# def Login():
#     if request.method == 'GET':
#         return render_template('login.html');
#     elif request.method == 'POST':
#         username = request.form.get('username');
#         password = request.form.get('password');#这里是POST的参数 通过HTML传来 属性里面的name定位
#         # request.args.get('3123122') #这里是GET类型的参数 GET类型的参数是通过url传来的
#         return render_template('Login.html',username = username,password = password);

# @appIns.route('/get/<name>')
# def Get(name):
#     return session.get('username');

# @appIns.route('/register', methods=['POST','GET'])
# def Register():
#     pass;

# @appIns.route('/test')
# def Test():
#     return render_template('Test.html');


# @appIns.before_request
# def my_before_request():
#     print('my_before_request');

import Config;
App = Flask(__name__,template_folder="../templates"); #如果找不到html文件 这里可以指定模板的路径

@App.route("/")
def HomePage():
    url = url_for("About") #url反转，通过视图函数名查找对应的url（相对路径）

    # return redirect(url);   # 重定向 上面获取了About视图函数的url地址 这里直接使用这个地址 就转到对应的页面了

    context = {
        "name":"tangyao",
        "age":33,
    }

    books = [

        {
            "name":"三国演义",
            "price":333,
        },
        {
            "name":"水浒传",
            "price":108
        }
    ]

    fuck = 123;

    avatar = "../static/img/IronMan.jpg"

    return render_template("Main.html",a=fuck, books=books,avatar = avatar, **context);   # 一个参数可以用命名参数传递 参数多了用dict

@App.route("/about/")
def About():
    return "关于页";

@App.route("/about/info/")
def info():
    return "信息";

if __name__ == "__main__":
    # appIns.run();
    App.config.from_object(Config);
    App.run();




