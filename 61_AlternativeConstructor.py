#Constructor is the method that initialize the objects' attribute
#There are times when you may want to create an object in different ways
#Or with different initial values ,that is provided by the default constructor
#This is where we can use class method as alternative constructor

class fruits:
    def __init__(self,name,price):
        self.name=name
        self.price=price
        
    #This is Alternative Constructor or also called as class method as alternative constructor
    @classmethod
    def fromStr(cls,string):
        return cls(string.split(",")[0],int(string.split(",")[1]))
    
f1=fruits("Apple",200)
print(f1.name,f1.price)

enter=("Mango,150")
f2=fruits.fromStr(enter)
print(f2.name,f2.price)