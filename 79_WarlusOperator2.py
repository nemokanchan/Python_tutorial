#Warlus Operator(:=)

#Without warlus:
foods=list()
while True:
    food=input("Input food if you want to enter otherwise input quit:")
    if food=="quit":
        break
    foods.append(food)
print(foods)
    
    
#With Warlus:
while(food:= input("What food do you like:")!="quit"):
    foods.append(food)
    
print(foods)
    