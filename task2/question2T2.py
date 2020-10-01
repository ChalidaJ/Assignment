a=int(input("Enter the calculation option   "))
if a > 5 or a < 1:
    print("Out of scope")
else :
    x=int(input("Enter the first value    "))
    y=int(input("Enter the second value   "))
    if a == 5 :
        avg=(x+y)/2
        if avg < 0 :
            print("NEGATIVE")
        else :
            print("The result is", int(avg))
    elif a == 1 :
        addition=x+y
        if addition < 0 :
            print("NEGATIVE")
        else :
            print("The result is", (addition))
    elif a == 2 :
        subtraction=x-y
        if subtraction < 0 :
            print("NEGATIVE")
        else:
            print("The result is", (subtraction))
    elif a == 3 :
        division=x/y
        if division < 0 :
            print("NEGATIVE")
        else :
            print("The result is", (division))
    elif a == 4 :
        multi=x*y
        if multi < 0 :
            print("NEGATIVE")
        else :
            print("The result is", (multi))
    
















