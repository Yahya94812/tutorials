import csv #stands for "comma seperated values"

class Items:
    all=[]#class attribute
    def __init__(self,name,qt:float,mrp:int):
        self.name=name
        self.qt=qt
        self.mrp=mrp
        Items.all.append(self)

    def __repr__(self):#repr stand for "representing your objects"
        return f"Items('{self.name}',{self.qt},{self.mrp})"    
    
    @classmethod
    def instentiate_from_csv(cls):
        with open ("data.csv","r") as f:
            reader=csv.DictReader(f)#it read whole csv file and store it in multiple dictionary
            items=list(reader)
            for item in items:#items is a list of dictionary but item is a dictionary and get is used for accessing value from the key in dictionary
                Items(
                    name=item.get("name"),
                    qt=item.get("qt"),
                    mrp=item.get("mrp")
                    )
 

Items.instentiate_from_csv()    
print(Items.all)