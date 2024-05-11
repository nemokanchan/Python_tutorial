def func():
 try:
     l=[2,5,8,3,6]
     i=int(input("Enter the index:"))
     print(l[i])
     return 1
    
 except:
     print("some error occurred")
     return 0
 finally:
     print("I am always executed")
     
x=func()
print(x)