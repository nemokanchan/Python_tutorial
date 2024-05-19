class Company:
    # class variable:Common to all instance
    companyName="Amazon"
    size=0
    def __init__(self,name):
        self.name=name#instance variable and individual to every instance
        self.raise_amount=0.02
        Company.size +=1
    def display(self):
        print(f"Hey, I am {self.name}")
        print(f"I am working on {self.companyName}\n After my placement company size is {self.size}\n and my raise amout is {self.raise_amount}")
        print("\n")
    
emp1=Company("Nemo")
emp1.raise_amount=0.3
emp1.companyName="BigMart"
Company.companyName="Daraz"
emp1.display()

emp2=Company("Micky")
emp2.companyName="HamroBazar"
emp2.display()

emp3=Company("Jerry")
emp3.display()

        