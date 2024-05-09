marks={
    "maths":65,
    "English":87,
    "Toc":59,
    "Dsa":56
} 
marks2={
    "Ect":44,
    "EM" :59
}
marks.update(marks2)
marks2.clear()
print(marks)
print(marks2)
marks.pop("Toc")
print(marks)
marks.popitem()
print(marks)
del marks["maths"]
print(marks)
del marks
#IF we print then error appears
#Other methods can be study from documentation

