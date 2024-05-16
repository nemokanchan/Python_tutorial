class person:
    name="Kanxu"
    occ="Student"
    
    def __init__(self):
        print("///Constructor is called because object is created/////")
        print("I am a constructor and I run when the object is created")
        
    def info(self):
        print(f"{self.name} is a {self.occ}")
        
a=person()
print(a.name)
a.name="Bacchu"
a.info()
a.occ= "Software Engineer"
    
b=person("")