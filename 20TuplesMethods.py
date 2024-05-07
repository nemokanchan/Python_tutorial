#Tuples are immutable and if you want to change then convert into list
countries=("Spain","Nepal","India","China")
print(countries)
temp=list(countries)
temp.append("Russia")       #add item
print(temp)
temp.pop(2)                 #remove item
print(temp)
temp[3]="Finland"           #change item
countries=tuple(temp)
print(countries)

#We can create new tuple by adding two tuple
count2=("Pakistan","UAE","USA")
print("2nd tuple=",count2)
count3=countries+count2
print(count3)

#Count Method
tup1=(1,4,2,3,7,1,6,3,5,1,7)
print("No. of 1 :",tup1.count(1))
print("Index of 7:",tup1.index(7))#Gives index of 1st occurance of item
res=tup1.index(7,6,)#Here 7 is the no., 6:_ gives slicing of tuple between 6 to maxsize-1
print("Index of 7:",res)

print("Length of tuple:",len(tup1))