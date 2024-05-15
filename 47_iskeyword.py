#Both i'is' and '==' are comparision operator and return boolean result
a=4
b="4"

print(a is b)#exact location of object in memory
print(a==b)#value

c=[4,3,2,1]
d=[4,3,2,1]

print(c is d)
print(c == d)
#Due to two different list 1st one becomes false and they anre sam so 2nd becomes true
a=3
b=3
#Since 3 is constant and is immutable so both comparision operators point same location where 3 lies


print(a==b)            #campares value
print(a is b)         #compares identity

