


class myClass:
    id = -1;
    name = "noname";

    def __init__(self):
        print("类myClass 初始化。。。");
        self.id = 0;
        self.name = "init name";

    def __print(self):
        print(self.id);
        print(self.name);

    def output(self):

        self.__print();
        print(self.id);
        print(self.name);

class myMonster(myClass):
    skillid = 0;

    def __init__(self):
        myClass.__init__(self);
        print("类myMonster 初始化。。。");
        skillid = 1;


if __name__ == "__main__":
    

    m = myMonster();

    print(m.name);

