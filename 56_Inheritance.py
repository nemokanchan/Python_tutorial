class fruits:
    def __init__(self,name,color):
        self.name=name
        self.color=color
        
    def showDetails(self):
        print(f"The {self.name} has {self.color} color")
 
class vegetable(fruits):
    def showVeg(self):
        print("I am derieved from the class fruits ")
            
    
b=fruits("Apple", "red")
b.showDetails()
c=vegetable("Mushroom","White")
c.showVeg()
c.showDetails()#the object of derieved class can use the features of parent class