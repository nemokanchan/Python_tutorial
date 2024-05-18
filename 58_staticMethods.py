class Math:
    def __init__(self,num):
        self.num=num
        
        
    def addtonum(self,n):
        self.num=self.num+n
        
    @staticmethod#can run method without self and is indepedent to class
    def add(a,b):
        return a+b
    
# result=Math.add(1,2)
# print(result)

a=Math(5)
print(a.num)
a.addtonum(6)
print(a.num)

#both gives same and are same fot static method:
print(a.add(4,6))
print(Math.add(4,6))