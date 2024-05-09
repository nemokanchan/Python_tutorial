#Combination of Key Value PAirs 
dic={
    "Kabin":"Boy",
    "Kanchan":"Girl"
}
print(dic["Kabin"])
print(dic.get("Kabin"))#It doesnot give any error at any condition


dict={
    
    33:"KAnchan",
    44:"kabin"
}
print(dict)
print(dict.keys())

for key in dict.keys():
    print(dict[key])
    print(f"The value of {key} is {dict[key]}")
   
for key,value in dict.items():
    print(f"The value of key {key} is {value}") 
    
    