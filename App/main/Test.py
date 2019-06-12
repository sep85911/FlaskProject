import sys;
import os;
import re;

import string;
import datetime;
import calendar;
import time;
import json;

import tkinter;
from tkinter import Listbox;
from tkinter import messagebox;

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

import math;

def avg(myList):
    l = len(myList);
    all = 0;
    for i in myList:
        all = all + i;
    return all / l;

def drop_first_last(grade):
    fisrt,*middle, last = grade;    # *(星号表达式)表示这是一个列表类型 如果没有也会是一个空列表 并且可以和_（下划线）配合使用
    return avg(middle);

# print(drop_first_last(p));

from collections import deque


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


# Example use on a file
if __name__ == '__main__':
    with open(r'../../../Test20190601.txt') as f:
        for line, prevlines in search(f, 'python', 4):
            for pline in prevlines:
                print(pline, end='')
            print('-' * 20) #这是分割线


import heapq;

list001 = [4123,54,132,65,-423,534,999,4,13,];

print(heapq.nlargest(2,list001));#一个列表中最大的N项
print(heapq.nsmallest(3,list001));#一个列表中最小的N项

list002 = [
    {"name":"tangyao","age":18,"sex":False},
    {"name":"chenjing","age":23,"sex":True},
    {"name":"haha","age":2413,"sex":True},
    {"name":"tangxiaodong","age":12,"sex":False},
]

print(heapq.nlargest(2,list002,lambda a:a['age']))


print("{0}{1}{2}".format(1,5342,3)); #字符串格式化 里面用{}代替 可以加数字 也可以不加 不加就按顺序填充 其中！后面可以加s r a 分别对应str() repr() ascii()

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


q = PriorityQueue();

q.push(cItem("A"),2);
q.push(cItem("B"),5);
q.push(cItem("C"),3);
q.push(cItem("D"),44);
q.push(cItem("E"),13);

print(q.pop());


testlist = [];
heapq.heappush(testlist,-1);
heapq.heappush(testlist,-2);
heapq.heappush(testlist,-3);
heapq.heappush(testlist,-24);
heapq.heappush(testlist,-6);



d = defaultdict(list);
d["a"].append(1)
d["a"].append(2)
d["b"].append(3)
d["b"].append(4)

sd = defaultdict(set);
sd['a'].add(3)
sd['b'].add(4)
sd['a'].add(5)

from collections import OrderedDict;

oList = OrderedDict();
oList["fuck"] = 1;
oList["joker"] = 3;
oList["weaker"] = 2;
oList["sucker"] = 4;

for i in oList:
    print(i,oList[i]);