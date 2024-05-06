#Required argument
def sum1(a,b):
    print("Addition:",a+b)
    
sum1(3,6)

#Default Arguments:
def sum2(c=0,d=9):
    print("Addition:",c+d)
    
sum2()
sum2(3)
sum2(d=6)

#Keyword Arguments
def sum3(a,b):
    print("Addition:",a+b)

sum3(b=9,a=4)

#Variable length argument as tuple
def sum4(*n):
    sum=0
    for i in n:
        sum=sum+i
        average=(sum/len(n))
        print("Sum=",sum ,"Average=",average)
    
sum4(5,2,4,7)

#variable length as dictionary
def name(**name):
    print("Hello",name["fname"],name["lname"])
    
    
name(fname="Man", lname="Maya")