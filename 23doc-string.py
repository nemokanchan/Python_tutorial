#Doc-string are string literals that appears right after the defination of a function, method, class or module
#Comment doesnot change the output but change in the doc-string changes the output
 
def square(n):
    '''Take in a number n, returns the square of n'''
    print("Answer:",n**2)
     
 #Doc-strinf is always written at starting of function body    
square(5)
print(square.__doc__)

#PEP 8 is python enhancement proposal provides guideline and best platform to practice python code
#The Zen of python
#It can be achieved by using import this in python terminal
#and it prints few line that has important information for programmmers


