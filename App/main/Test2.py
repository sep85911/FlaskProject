# 侠义道II专用日志文件处理程序

#打包py为exe 安装并使用pyinstall 

import codecs;
import xlsxwriter;
import re
import os;
import sys;

if __name__ == "__main__":

    filetype = input("请输入要转换的格式（1:txt 2：xlsx）：");

    txt,xlsx = 0,0;
    if filetype == "1":
        txt = 1;
    elif filetype == "2":
        xlsx = 1;
    else:
        print("输入错误，结束程序");

    files = os.listdir(sys.path[0])
    rr = re.compile('官方___(.+)___(.+).txt')   #正则表达式 用于筛选成组的文件名
    filegroup = {};

    for filename in files:

        res = rr.findall(filename)  #提取模式需要findall函数 并且正则表达式里有() 
        if res:
            a = list.pop(res)

            serverName = a[0];
            logName = a[1];

            if not logName in filegroup:    #如果已经有文件名了
                filegroup[logName] = [];    #如果没有文件名 在字典中以log名为索引创建列表
            
            list.append(filegroup[logName],serverName)
    
    if xlsx == 1:
        for key in filegroup:
            workbook = xlsxwriter.Workbook(key + ".xlsx"); #xlsx文件
            worksheet = workbook.add_worksheet(key); #xls文件里的sheet
            head = "账号	ID	角色	服务器	等级	日期	时间	项目1	项目2"
            resHead = str.split(head,"	");
            index = 0;            

            for i in resHead:                
                if i.isdigit():
                    worksheet.write_number(0,index,int(i));# 行 列  内容#
                else:
                    worksheet.write_string(0,index,str(i));# 行 列  内容#

                index = index + 1;

            lineIndex = 1;
            nextAdd = 0;
            for resfile in filegroup[key]:
                with codecs.open(sys.path[0]+"\\"+"官方___"+resfile +"___"+key+".txt","r","gb18030") as ff:
                    singleText = ff.readlines();
                    for line in singleText:

                        if not str.startswith(line,"中游"): 

                            if nextAdd == 1:
                                nextAdd = 0;
                                lines = "中游" + line[:-1]
                            else:
                                lines = line[:-1];

                            resLine = str.split(lines,"	");
                            rowIndex = 0;
                            for i in resLine:
                                if i.isdigit():
                                    worksheet.write_number(lineIndex,rowIndex,int(i));#行 列 内容#
                                else:
                                    worksheet.write_string(lineIndex,rowIndex,str(i));#行 列 内容#

                                rowIndex = rowIndex + 1;
                            lineIndex = lineIndex + 1;
                        else:
                            nextAdd = 1;
                        

            workbook.close();
    elif txt == 1:
        for key in filegroup:
            with open(key+".txt","w") as f:
                head = "账号	ID	角色	服务器	等级	日期	时间	项目1	项目2\n"
                f.write(head);
                for resfile in filegroup[key]:
                    with codecs.open(sys.path[0]+"\\"+"官方___"+resfile +"___"+key+".txt","r","gb18030") as ff:
                        singleText = ff.readlines();
                        for line in singleText:
                            f.write(line);
                            f.flush();
                f.close();
