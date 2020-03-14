import glob;


class CObject:
    _id = 0;
    _name = "noname";

    def __init__(self):
        self._id = 0;
        self._name = "init name";

    @property
    def ID(self):
        return self._id;

    @property
    def Name(self):
        return self._name;

    @ID.setter
    def ID(self, id):
        if id > 10000:
            print("id太大了，无法设置");
            return;

        self._id = id;

    @Name.setter
    def Name(self,name):
        if name == "fuck":
            print("脏话！无法设置");
            return;
        
        self._name = name;

class CCreature(CObject):

    hp = 100;
    mp = 100;
    sp = 100;

    def funcname(self):
        pass

class CTest:
    __slots__ = ("name","id");
    


    # def __init__(self):
    #     myClass.__init__(self);
    #     print("类myMonster 初始化。。。");
    #     skillid = 1;

import os;
import calendar;
import shutil;
import glob;
import random;

import lxml;

import venv;


def log(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print("This is %s" % text);
            return func(*args,**kw);
    
        return wrapper;
    return decorator;

@log("first print")
def testfunc():
    print("This is testfunc");


class CTest002:
    __slots__ = ["go"];

if __name__ == "__main__":
    
    obj = CTest002();
    obj.go = 321;

    print(obj.go);



