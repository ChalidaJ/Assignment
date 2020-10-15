from functools import reduce

lists = [[1, 2, 3], [4, 5], [6, 7, 8]]
add = lambda x, y: x+y
newlist = reduce(add, lists)

print(newlist)
