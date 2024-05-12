#Its is inbuilt function by python 

marks=[32,67,34,65,12,78,36,39,45]
index=0
for mark in marks:
    print(mark)
    if(index==5):
        print("Welldone,Highest marks")
    index+=1
 #With enumerate function   
for index, mark in enumerate(marks, start=3):
    print(mark)
    if(index==8):
        print(f"Welldone,Highest marks is {mark}")
        

    