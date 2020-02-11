import sys;
import os;
import re;

import string;
import datetime;
import calendar;
import time;
import json;

import math;
import heapq;
import tkinter;

from tkinter import Listbox;
from tkinter import messagebox;
from collections import deque
from collections import defaultdict;


# 脚本所在文件夹
Script_folder = "E:\\xydII\\WorldServer\\Script";

# def CheckTaskID(address):
#     for filename in os.listdir(Script_folder):
#         print(filename);


def DelMore(nums):
    length = len(nums);

    index = 0;

    while(index + 1 < length):
        start = index;
        for i in range( index + 1, length):
            if nums[start] == nums[i]:
                del nums[i];
                # index += 1;
                length = len(nums);
                break;
            else:
                if i == length - 1:
                    index += 1;
                    break;
    return len(nums);

def showmessage(a,b,c):
    with open("static/json/jsontest.json","r") as f:
        text = f.read();
        myJson = json.loads(text);  # 用json.loads函数将json内容转化为dict
        print(myJson)
        
        c = myJson["passes"][0]["shader"]
        # print(c);

def showOneMsg():
    print("Testing!")
    
# if __name__ == "__main__":
    
#     top = tkinter.Tk();    

#     screenW = top.winfo_screenwidth();
#     screenH = top.winfo_screenheight();
#     selfW = 100;
#     selfH = 60
#     size = "%dx%d+%d+%d" %( selfW,selfH,(screenW - selfW) / 2, (screenH - selfH) / 2 );
#     top.geometry(size);

#     b = tkinter.Button(top, text="测试",command=lambda : showmessage(a=1, b=2, c=3))    
#     b.pack(expand="yes");

    # print("按下测试键开始...")
    # top.mainloop();

#     print("按下测试键开始...")
#     top.mainloop();


abc = 312313;

p = (11,22,33,44)

# aa,bb,cc = p;

# print(cc)   # 解压赋值 前后数量应该一致 不一致就报错 可以用_（下划线）作为占位符 忽略不需要的值

def Test002():
    print(__name__);


def avg(myList):
    l = len(myList);
    all = 0;
    for i in myList:
        all = all + i;
    return all / l;

def drop_first_last(grade):
    fisrt,*middle, last = grade;    # *(星号表达式)表示这是一个列表类型 如果没有也会是一个空列表 并且可以和_（下划线）配合使用
    return avg(middle);

def search(lines, pattern, history=3):
    previous_lines = deque(maxlen=history)  #双向队列 append从右边加 appendleft从左边加 maxlen限定了最大容量 超过的话 另一边的第一个将被挤出去
    for line in lines:
        if pattern in line:#在每一行中查找
            previous_lines.append(line)
            yield line, previous_lines #返回出去

def TestItertor(a):
    while a <= 10:
        yield a;    #迭代 用于泛型for
        a = a + 1;

class cItem:
    def __init__(self,name):
        self.name = name;

    def __repr__(self):#重写这个函数后 可以打印值 
        return "class cItem({!r})".format(self.name);   

    def __lt__(self,other): #重写这个函数后 类可以支持大于小于判断
        return self.name < other.name;
        
class  PriorityQueue:
    def __init__(self):
        self._queue = [];
        self._index = 0;

    def push(self,item,priority):
        heapq.heappush(self._queue,item);
        self._index += 1;

    def pop(self):
        return heapq.heappop(self._queue);

# 摄氏度转化为华氏度
def TempExchange(nTemp):
    # c = float(input("输入摄氏度:"));
    f = 1.8 * nTemp + 32;
    print("华氏度为：{}".format(f));

# 判断是否为回文数
def isHui(nNum):
    temp = nNum;
    total = 0;
    while temp > 0:
        total = total * 10 + temp % 10; #取temp的最后一位和total拼接起来形成倒序数字
        temp //= 10;
    return total == nNum;   #判断是否和之前的数字一样

# RPG文字
def horsewords(showmsg):
    allWords = "这是一段测试文字，呵呵呵";
    curWords = "";
    for i in range(len(allWords)):
        print(allWords[0:i])
        time.sleep(0.5);
        os.system("cls");

def fib(num):
    a,b = 0,1;
    for i in range(num):
        a,b = b, a + b; 
        yield a;
   
def main():
    # for i in fib(10):
    #     print(i)

    tTemp = (1,2,3,4,5,6,7,8,9)

    for i in range(len(tTemp)):
        print("找到一个偶数：{}".format( tTemp[i] ) if tTemp[i] % 2 == 0 else "奇数，滚蛋！")

def TestTuple():
    myTuple001 = (1,2,3,4,5)
    print(myTuple001[3]);
    # myTuple001[0] = 43;   # tuple不允许修改

def TestSet():
    mySet001 = {1,2,3,4,5}
    mySet002 = {3,4,5,6,7,8}

    mySet001.update([8,9,1]);

    print(mySet001);



def print_board(board):
    print(board["TL"]+"|"+board["TM"]+"|"+board["TR"]);
    print("-+-+-");
    print(board["ML"]+"|"+board["MM"]+"|"+board["MR"]);
    print("-+-+-");
    print(board["BL"]+"|"+board["BM"]+"|"+board["BR"]);

def play_board():
    init_board={
        "TL":" ","TM":" ","TR":" ",
        "ML":" ","MM":" ","MR":" ",
        "BL":" ","BM":" ","BR":" "
    }
    begin = True;

    while begin:
        cur_board = init_board.copy();
        turn = "x"
        counter = 0;
        begin = False;
        os.system("cls");
        print_board(cur_board);
        while counter < 9:
            move = input("该{}走了，请输入想要下的位置号:".format(turn));
            if cur_board[move] == " ":
                counter += 1;
                cur_board[move] = turn;
                if turn == "x":
                    turn = "o";
                else:
                    turn = "x"
            os.system("cls");
            print_board(cur_board);
        
        choice = input("再玩一局？YES/NO");
        begin = choice == "YES";

class Test:
    def __init__(self):
        self._NAME = "name1";
        self._ID = 123;

    @property
    def Name(self):
        return self._NAME

    @Name.setter
    def Name(self,name):
        self._NAME = name;

    @property
    def ID(self):
        return self._ID;

    @ID.setter
    def ID(self,id):
        self._ID = id;

from abc import ABCMeta,abstractmethod; #python中抽象类需要导入abc模块中的ABCMeta 和 abstractmethod; 使用后该类将不能被实例化
class myClass(object,metaclass=ABCMeta):
    def __init__(self):
        pass;

    @abstractmethod
    def run(self):
        print("run")

if __name__ == "__main__":
    # horsewords("这是一段走马灯文字");

    # main()

    # TestTuple();

    # TestSet();

    # play_board();]

    # Test_Obj();
    



