#Constructor is a special method to create and initialize object of a class
#Constructor is called automatically when object is created
#Constructor are of two types :Default and parameterized
class person:
    name="Kanxu"
    occ="Student"
    
    def __init__(self,n,o):
        print("****Constructor called*****")
        self.name=n
        self.occ=o
        
    def info(self):
        print(f"{self.name} is a {self.occ}\n\n")
        
a=person("Alisha","Dancer")
a.info()

c=person("Ajita","Model")
c.info()

    
b=person("Aagya","Actress")
b.info()