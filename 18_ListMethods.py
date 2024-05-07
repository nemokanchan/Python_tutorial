l=[1,3,2,4,6,0,66,90,1,65,33]
print(l)
l.append(76)
print(l)
l.sort()
print(l)
l.reverse()
print(l)
print(l.index(1))#gives index of first occurance
print(l.count(1))

m=l.copy()
m[0]=0
print(l)

l.insert(1,899)#1=index, 899=data
print(l)

n=[77,66,44]
k=l+m
print(k)
l.extend(m)
print(l)

