#'r' is a read mode and read mode is default also.
#and only we can read file after using read mode
#Also we can usre other mode and use them like using 'w' mode we can write and can create new file if not exist
#We can use append mode as 'a' and can add other content on the file
#create (x):can create new file if not already exist
#binary(b):to open binary file

#READING A FILE
f=open('myfile.txt','r')
print(f)
text=f.read()
print(text)
f.close()

s=open('myfile.txt','w')
s.write("I am adding new text")
s.close()

h=open('myfile.txt','a')
h.write(" I am a good girl/boy")
h.close()
#'with' statement automatically close the file as you are done with it.
with open('myfile.txt','a') as f:
    f.write("\n Hey I am inside with")
    
