from flask import render_template,Blueprint;

from .Extensions import db;
from App import Models;

bp = Blueprint("main",__name__);

@bp.route("/")
def HomePage():
    return render_template("Main.html");   # 一个参数可以用命名参数传递 参数多了用dict

@bp.route("/myblog/")
def About():
    newUser = Models.User(username="fucker",age = 123);
    db.session.add(newUser);
    db.session.commit();
    return render_template("MyBlog_Main.html")

@bp.route("/about/info/")
def info():

    return "信息";

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