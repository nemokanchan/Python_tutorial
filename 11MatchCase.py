day=str(input("What day is today? \n"))
match day:
    case 'Sunday':
        print("Today is Sunday.")
    case 'Monday':
        print("Today is Monday.")
    case 'Tuesday':
        print("Today is Tuesday.")
    case 'Wednesday':
        print("Today is wednesday.")
    case 'Thursday':
        print("Today is Thursday.")
    case 'Friday':
        print("Today is Friday.")
    case 'Saturday':
        print("Today is Saturday.")
    case _ if day!='holiday':
        print("Invalid and is not even Holiday")
    case _ if day=='Holiday':
        print("It's Holiday")    
    case _ :
        print("Totally invalid")