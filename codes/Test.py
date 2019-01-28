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

import bs4;
    
if __name__ == "__main__":
    
    # top = tkinter.Tk();    

    # screenW = top.winfo_screenwidth();
    # screenH = top.winfo_screenheight();
    # selfW = 100;
    # selfH = 60
    # size = "%dx%d+%d+%d" %( selfW,selfH,(screenW - selfW) / 2, (screenH - selfH) / 2 );
    # top.geometry(size);

    # b = tkinter.Button(top, text="测试",command=lambda : showmessage(a=1, b=2, c=3))    
    # b.pack(expand="yes");


    # print("按下测试键开始...")
    # top.mainloop();

    print(bs4.__version__)


   
