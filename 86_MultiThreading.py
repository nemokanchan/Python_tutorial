import threading
import time
from concurrent.futures import ThreadPoolExecutor
def func(seconds):
    print(f"sleeping for {seconds} seconds ")
    time.sleep(seconds)
    
def main():
    time1=time.perf_counter()
    print(f"Time for function {time1}")
   
        #Normal code 
        # func(4)
        # func(2)
        # func(1)


    #Same code using threading
    t1=threading.Thread(target=func,args=[4])
    t2=threading.Thread(target=func,args=[2])
    t3=threading.Thread(target=func,args=[1])

    t1.start()
    t2.start() 
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    #Calculating time
    time2=time.perf_counter()
    print(f"Total time {time2}")
    t=time2-time1
    print(f"Time to execute threading {t}")

def poolingDemo():
    with ThreadPoolExecutor() as executor:
    #   future1 = executor.submit(func, 3)
    
    #   future2 = executor.submit(func, 5)
    #   future3 = executor.submit(func, 2)
    #   print(future1.result())
    #   print(future2.result())
    #   print(future3.result())
      l =[3 ,5, 2]
      results=executor.map(func,l)
      for re in results:
          print(re)
    
poolingDemo()  
    