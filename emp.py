class Employee:
    name="Kanchan"
    
    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i
   
    def __str__(self):
        return f"The name of the employee is {self.name}"
    #If the code doesnot found str function repr is called
    def __repr__(self):
        return f"The name of the employee is {self.name} repr"
    
    def __call__(self):
        print("Hey, How are you?")