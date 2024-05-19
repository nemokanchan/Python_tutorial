#The dir function returns all the list of attributes and methods avaiable for object

x=[1,2,3]
print(dir (x))

#   __dict__ attribute:returns a dictionary representation of an objects attribute
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
p=person("Bacchu",20)
print(p.__dict__)

# help method ::help():used to get help documentation for object
print(help(person))