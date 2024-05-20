class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        
class programmer(Employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang=lang
        print(f"I am {self.name} , my id is {self.id} and I am expertise of {self.lang}")
        
        

nemo=Employee("Nemo",3)
kabin=programmer("Kabin",1,"Java")
print(kabin.name)
print(kabin.id)
print(kabin.lang)
