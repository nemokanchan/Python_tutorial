f=open('myfile.txt','r')
i=0
while True:
    i=i+1
    line=f.readline()
    if not line:
        break
    m1=line.split(",")[0]
    m2=line.split(",")[1]
    m3=line.split(",")[2]
    print(f"MArks of s {i} in Maths is:{m1}")
    print(f"MArks of s {i} in DS is:{m2}")
    print(f"MArks of s {i} in Sost is:{m3}")
    if not line:
        break
    
    
f=open('file2.txt','w')
lines=['line1\n','line2\n']
f.writelines(lines)
f.close