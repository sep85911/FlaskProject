class CMyClass:

    __name = ""
    __id = 0;

    def __init__(self):
        self.__id = 0;
        self.__name = "inited name";

        self.a = 0;
        self.b = 1;

    def __str__(self):
        return "fuck yourself";

    @property
    def ID(self):
        return self.__id;

    @ID.setter
    def ID(self,num):
        if num < 0:
            print("暂不支持设置ID为负值");
            return
        self.__id = num;    

    # 以下两个函数写了可以让类的对象可以在范型for里进行迭代
    def __iter__(self):
        return self;

    def __next__(self):
        self.a,self.b = self.b, self.a + self.b;
        if self.a > 1000: # 退出条件
            raise StopIteration;

        return self.a;

if __name__ == "__main__":
    aaa = CMyClass();
    aaa.ID = -123;
    print(aaa.ID);
    aaa.ID = 321;
    print(aaa.ID);

    print("Fib Starting");
    for i in aaa:
        print(i);