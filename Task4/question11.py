li = [1,2,3,4,5,6,7,8,9,10]

x = filter(lambda   x: x%2==0, li)
y = list(map(lambda x: x**2, x))
 
print(y)
 