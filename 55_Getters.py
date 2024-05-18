#Using @property we can 

class MyClass:
    def __init__(self, value):
        self._value= value
        
    def show(self):
        print(f"Value is {self._value}")
        
    @property#Using this we can use method as objects' property and it is called getters
    def ten_value(self):
        return 10* self._value
    @ten_value.setter#Using these we can set new value of getter
    def ten_value(self,new_value):
         self._value=new_value+3    
    
    
obj = MyClass(10)
print(f"The value using getter is {obj.ten_value}")
obj.ten_value=96
print(obj.ten_value)
obj.show()
