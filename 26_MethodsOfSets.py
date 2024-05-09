s1={3,6,8,4,2}
s2={9,5,8,1}
print(s1.union(s2))
print(s1, s2)
# s1.update(s2)
# print(s1,s2)
# print(s2.intersection(s1))
# print(s1.intersection_update(s2))
#Symmetric difference of a and b=(a-b)+(b-a)
#Symmetric difference of a and b=(a union b)-(a intersection b)

s3=s1.symmetric_difference(s2)
print(s3)
s3=s1.difference(s2)
print(s3)

#isdisjoint checks if items in given sets present in another set
print(s1.isdisjoint(s2))
#issuperset: Checks superset  and also there is issubset method
print(s1.issuperset(s2))

s2.remove(1)
#remove can be replaced by discard() that it doesnot throw error as pass in function
s4={3,24,5}
i=s4.pop()
print(s4)
print(i)
#del delets the entire set
del s4
#print(s4) gives error
s3.clear()#It clears all the item

if 1 in s1:
    print("Present")
    



