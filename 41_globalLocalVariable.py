#Local variable: The variable that is defined and accessible only inside the function
#Global variable:The variable that is defined 
x=5 #global variable
print("Global variable at first=",x)

def fun():
    global x #Local x is made global so global x becomes 9
    x=9
    y=8
    print("Variable y =",y)
    
fun()
print("After changing global variable locally:",x)
