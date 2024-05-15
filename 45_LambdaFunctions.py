#Instead of this :::::::::::::
# def double(x):
#     return x*2

#WE can do THis:::::::Using lambda function
#Lambda function is one line function used when we need diffrent small functions of simple calculations

def oaky(fx,val):
    return fx(val)
double =lambda x:x*2
cube=lambda x:x*x*x
avg =lambda x,y:(x+y)/2
print(double(6))
print(cube(7))
print(avg(2,6))


print(oaky(lambda x:x*x ,2))