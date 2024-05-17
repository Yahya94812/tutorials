class Items:
    all=[]#class attribute
    def __init__(self,name,qt,mrp):
        self.name=name
        self.qt=qt
        self.mrp=mrp
        Items.all.append(self)

    def __repr__(self):#repr stand for representing your objects
        return f"Items('{self.name}',{self.qt},{self.mrp})"    

    @classmethod
    def hello(cls):
        print("hello i am in class method")

item1=Items("cpu",1,1000)
item2=Items("keys",3,100)
print(Items.all)

for i in Items.all:
    print(i.name)

for i in Items.all:
    print(i.qt)

Items.hello()