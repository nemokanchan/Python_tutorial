l=[4,3,2,9,"yes","allow"]
print(l)
print(type(l))
print(l[2])
print(l[0])
print(l[4])
print(l[-3])#negative index length-3 i.e 6-3

if 3 in l:
    print("Present")
    
if "ab" in 'Kabin':
    print("yesss")
    
print(l)
print(l[:])
print(l[2:5])
print(l[1:5:2])#jump index also involved

#LIST COMPREHENSION
lst=[i for i in range(5)]
print(lst)
lst=[i*i for i in range(8) if i%2==0]
print(lst)
