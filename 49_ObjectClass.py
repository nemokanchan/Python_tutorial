class person:
    #data:
    name="Kanxu"
    occupation="Student"
    age="22"
    def info(self): #function defination 
        print(f"{self.name} is a {self.occupation}")
        
    
        
    
#self ::It is a reference to a instance of a class and used to access variables that belongs to the class


    
a=person()
b=person()#creating object "a" of class person
print(a.name,a.occupation)

a.name="Kabin"
a.occupation="Teacher"
print(a.name,a.occupation)
a.info()#function call using object 'a'

b.name="Asmi"
b.occupation="Youtuber"
b.info()
