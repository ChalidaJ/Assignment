x='one-two-three-four-five-six'
 
items=[n for n in x.split('-')]
items.sort()
print('-'.join(items))


