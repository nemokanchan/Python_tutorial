class Base:
    def show(self):
        print("I am a human.")
        
class derived(Base):
    def show1(self):
        print("I am a Learning.")
        
class derived2(derived):
    def show2(self):
        print("I am learning python.")
        
a=derived2()
a.show()
a.show1()
a.show2()