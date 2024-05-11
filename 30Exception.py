a=input("Enter any number:")
print(f"Multiplication table of {a} is:")

try:
  for i in range(1,11):
   print(f"{int(a)}*{i}= {int(a)*i}")

    
except ValueError:
    print("Some value error occurred")  

except IndentationError:
    print("Some indentaton error occurred")
    
except IndexError:
    print("Some index error occured") #If a=[2,4] and 5 is entered
except:#can be writ as:except Exception as e:
    print("Sorry some error occurred") 

print("End of Program")

