#When a class inherits from a parent class,it can be override or extend the methods defined in parent class.
#However, sometimes you might want to use parent class method in the child class.
#This is where the super() keyword is used.

class parentclass:
    def parent_method(s):
        print("This is the parent method.")
        
class ChildClass(parentclass):
    def parent_method(s):
        print("parent method in child class")
        super().parent_method()
    def child_method(s):
        print("This is child method.")
        
        super().parent_method()
        
child_obj=ChildClass()
child_obj.child_method()
child_obj.parent_method() 
    
