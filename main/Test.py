import sys;
import os;
import re;

# 脚本所在文件夹
Script_folder = "E:\\xydII\\WorldServer\\Script";

def CheckTaskID(address):
    for filename in os.listdir(Script_folder):
        print(filename);


if __name__ == "__main__":
    # CheckTaskID(Script_folder);

    testStr = '"12345"';


    myre = re.compile("\d+",flags=0);

    myre.search(testStr);
    print(testStr);