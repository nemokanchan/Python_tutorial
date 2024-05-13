import os
#To rename 
for i in range(1,5):
  os.rename(f"data/Day{i}",f"data/RenamedFolder{i}")
    
#To print the list of folders in data
folders=os.listdir("data")

print(folders)
#To print the working directory
print(os.getcwd())