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
        if pattern in line:
            previous_lines.append(line)
            yield line, previous_lines

# Example use on a file
if __name__ == '__main__':
    with open(r'../../../Test20190601.txt') as f:
        for line, prevlines in search(f, 'python', 4):
            for pline in prevlines:
                print(pline, end='')
            print('-' * 20) #这是分割线


