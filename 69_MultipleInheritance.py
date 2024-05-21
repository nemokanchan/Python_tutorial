class Employee:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"The name is {self.name}")

class Singer:
    def __init__(self,song):
        self.song=song
        
    def show(self):
        print(f"The song is {self.song}")
    

class SingerEmployee(Employee,Singer):
    def __init__(self,name,song):
        self.name=name
        self.song=song
        
a=SingerEmployee("Kabina","Love_ME_Like_U_Do")
a.show()
print(SingerEmployee.mro())
