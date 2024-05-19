'''If we want to change or update the class variable originally
we can use class method and a normal function becomes class method
when we use decorator i.e "@classmethod" '''
class Company:
    companyName="Amazon"
    #Normal function than is used and change by changing instance
    def display(self):
        print(f"Hey, I am {self.name} and I am working on {self.companyName}")
    @classmethod#If it is not used then the name only change for instance
    def changeCompany(cls,newCompany):
        cls.companyName=newCompany

emp1=Company()
emp1.name="Nemo"
emp1.display()
print(f"By default name of company is {Company.companyName}")
emp1.changeCompany("Daraz")
emp1.display()
print(f"The new name of company is {Company.companyName}")