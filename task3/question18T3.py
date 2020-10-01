x="hello my name is abcd"
x=x.split(' ')

for word in x :
    if len(word) % 2 == 0 :
        print(word)
