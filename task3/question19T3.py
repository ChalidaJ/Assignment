from itertools import product, permutations
x=[1,2,3,4,5,6,7,8,9,-1]
target_number = 8

solutions = [pair for pair in permutations(x, 2) if sum(pair) == 8]
print('The pair of numbers whose sum equals to 8 :', solutions)
