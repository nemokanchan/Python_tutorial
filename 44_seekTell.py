with open('file.txt','r') as f:
    print(type(f))
    
    #move to the 10th byte
    f.seek(5)
    #Read the net 4 bytes
    print(f"The position of cursor is:{f.tell()}")#returns the current position
    data=f.read(4)
    print(data) 
    
#Only given byte of code will reamins in the fil
with open("file.txt",'w') as s:
    s.write("\n Happy to see you")
    s.truncate(10)
    
    
    
