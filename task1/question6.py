user_input = input("Enter a value ")

print("\n")
try:
    val = int(user_input)
    print("the data type is", type(val))
except ValueError:
    try:
        val = float(user_input)
        print("the data type is", type(val))
    except ValueError:
        print("the data type is <class 'string'>")


