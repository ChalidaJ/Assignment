x=[1,2,3,4,5,6,7,8,9]
x.sort()
for i in x :
    if (i%2 == 0):
        x.remove(i)
print(x)

