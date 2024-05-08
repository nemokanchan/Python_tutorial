#factorial(5)=5*4*3*2*1
#factorial(4)=4*3*2*1
#Factorial(0)=1
#Factorial(n)=n*(n-1)

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
    
print("Factorial of 5 is:",factorial(5))
