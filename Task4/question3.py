def unique_element(e):
  x = []
  for i in e:
    if i not in x:
      x.append(i)
  return x

print(unique_element([5,5,6,7,8,8,9,9,10])) 
