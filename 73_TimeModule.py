#Time module:Sets of operation to work with time related operation
import time

def usingWhile():
    i=0
    while i<50:
        
        i=i+1
        print(i)

def usingFor():
    for i in range(50):
        print(i)
        
        
init=time.time()

usingFor()
t1=time.time()-init
init=time.time()
usingWhile()
print(t1)

print(4444444444)
time.sleep(3)
print("I am running after 3 sec")

t=time.localtime()
formatted_time=time.strftime("%Y-%m-%d %H:%M:%S",t)
print(formatted_time)

