import glob;


class CObject:
    id = 0;
    name = "noname";

    def __init__(self):
        self.id = 0;
        self.name = "init name";

    def GetID(self):
        return self.id;

    def GetName(self):
        return self.name;

class CCreature(CObject):

    hp = 100;
    mp = 100;
    sp = 100;

    def funcname(self):
        pass

    


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


if __name__ == "__main__":
    

    # print(glob.glob(os.curdir + "/*.*"));

    #yy = int(input("请输入年份:"));
    #mm = int(input("请输入月份:"));

    noRepeatList = random.sample([i * 10 for i in range(10)],6);#采样 取不重复的n项

    print(noRepeatList)

    # 显示日历

    # print(calendar.month(yy,mm));



