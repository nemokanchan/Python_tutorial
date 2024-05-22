class A:
    def showA(self):
        print("I am class A.")
    
class B(A):
    def showB(self):
        print("I am class B derived from A.")
    
class C(A):
    def showC(self):
        print("I am class C derived from A.")
    
    
class D(B):
    def showD(self):
        print("I am class D derived from B.")
        
class E(B):
    def showE(self):
        print("I am class E derived from B.")
        
class F(C):
    def show(self):
        print("I am class F derived from C.")
        
    
obj=F()
obj.show()
obj.showA()