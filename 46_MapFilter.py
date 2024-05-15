#MAP:Takes sequence of elements and returns sequence of elements
     #It is higher order function
def cube(x):
    return x*x*x

print(cube(8))

l=[4,6,9,2,3,5]
# newl=[]
# for item in l:
#     newl.append(cube(item))
   

newl=list(map(cube,l)) 
print(newl)  

# FILTER: a function that returns elements that meets the given predicate
#It is higher order function
def filter_fun(a):
    return a>4

newl2=list(filter(filter_fun,l))
print(newl2)

# REDUCE :It should be imported from functools 
# higer order function that reduces the given code as
from functools import reduce
sum=reduce(lambda x,y:x+y,l)
print(f"Sum of the given list is {sum}")
