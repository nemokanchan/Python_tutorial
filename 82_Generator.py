#Generators are the special type of function that helps
# to generate an iterable sequence of values
#The yield statement returns a values from the generator 
def my_generator():
    for i in range(50):
        yield i
        
gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

for j in gen:
    print(j)
