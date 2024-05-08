#Instead of Format Function, We can use f-string
let="Hey {0}, I am also {1} and {2} to meet you"
feel="Nice"
name="John"
prof="student"
print(let.format(name,prof,feel))#Here,we should pass acc to index

#after using f-string
print(f"Hey {{name}}, I am also {{prof}} and {{feel}} to meet you")
print(f"Hey {name}, I am also {prof} and {feel} to meet you")
price=87.32214
txt=f"For only {price:.2f} dollers"

print(txt)
#print(txt.format())
