# a="KAnchan"
# for character in a:
#     print(character)

#string SLICING
names="Kabin,Kanchan"
print(len(names))
# including 0 but not 6 
print(names[0:6])
print(names[:6])
print(names[0:-3])
print(names[0:len(names)-3])
#if we want to use '-n' It implicitly use len(..)-n
print(names[-3:-1])
print(names[-1:-3])
