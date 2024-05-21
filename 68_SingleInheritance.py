class animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
        
    def make_sound(self):
        print("Sound made by animal.")
        
class dog(animal):
    def __init__(self, name,breed):
        animal.__init__(self,name,species="Dog")
        self.breed=breed
    def make_sound(self):
        print("Bark!!")
        # return super().make_sound()
        
d=dog("dog","Doggerman")
d.make_sound()

a=animal("dog","dog")
a.make_sound()