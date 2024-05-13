#The if __name__="__main__": is a idiom 
#IIIT is a common pattern used in python program to determine whether the script is
#run directly or being imported as a module into another script
def Kanchan():
    print("I love to learn Python")
    print(__name__)#Print main if directly executed otherwise prints name of this class

print(__name__)
if __name__ =="__main__":
   Kanchan()
    