while True :
    guess=int(input('Guess the Lucky Number   '))
    x="Y"
    y="N"
    if guess == 5 :
        break
    if guess != 5 :
        ask=str(input("Try again? Y/N:   "))
        if ask == x :
            continue
        if ask == y :
            break
        else :
            continue   

print("Game over!")
    




