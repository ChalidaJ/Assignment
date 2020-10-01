x="consul12"
digits=letters=0

for c in x :
    if c.isdigit():
        digits=digits+1
    if c.isalpha() :
        letters+=1
    else :
        pass

print("letters:   ", letters)
print("Digits:   ", digits)







