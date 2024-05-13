import os

if(not os.path.exists("data")):
    os.mkdir("data")#It creates a folder "data"

for i in range(1,5):
     #Here 1,5 is the range so 4 folders will created inside data
    os.mkdir(f"data/Day{i}")#it creates sub folder inside data as the the amount of range
    


