counter=0

while counter <5:
    number =int(input("Guess the Lucky number:  "))
    if number == 9  :
        print ("Good Guess")
        break
    elif number == " " :
        print("Sorry but that was not succesful")
    else :
        print("Try again")
    counter=counter +1
      








