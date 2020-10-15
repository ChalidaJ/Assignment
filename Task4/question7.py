
def compare_strings_len(a,b):
    
    if len(a) != len(b):
        x= max(a, b, key=len)
        print("The max lenght string is  ", x)
      
    elif len(a) == len(b):
        print(a)
        print(b)

compare_strings_len("Today is Thursday","Tommorow is Friday")

