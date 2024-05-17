#Decorator helps to modify the function
def greet(fx):
    def mfx(*args, **kwargs):
        print("Good morning")
        fx(*args, **kwargs)
        print("Bye")
    return mfx

@greet

def hello():
    print("Hello World")
    
hello()
#We can also run as 
#greet(hello)() if we do not defined @greet as above


#practicle use case
def add(a,b):
    print(a+b)
    
greet(add)(2,7)

