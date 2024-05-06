def calculateGmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)
    
def Compare(a,b):
    if(a>b):
        print("First no. is greater")
    elif(a==b):
        print("Equal Numbers")
    else:
        print("Second no is less than first")
calculateGmean(2,7)
Compare(3,3)
Compare(9,3)
calculateGmean(7,34)

#can be ignore error by using pass in function body
def hero():
    pass
