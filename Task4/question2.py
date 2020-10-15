def string_test(s):
    upper_case=0
    lower_case=0
    for i in s:
        if i.isupper():
            upper_case+=1
        elif i.islower():
            lower_case+=1
        else:
            pass
    
    print("The original string is  ", s)
    print("No. of uppercase is    ", upper_case)
    print("No. of lower case is  ", lower_case)


string_test("Today is a Rainy Day")

