class A:
    def show(self):
        print("I am class A.")
    
class B(A):
    def show(self):
        print("I am class B.")
    
class C(A):
    def show(self):
        print("I am class C.")
    
    
class D(B,C):
    def show(self):
        print("I am class D.")
    
obj=D()
obj.show()