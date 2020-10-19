<<<<<<< HEAD
x=open("demo.txt", "r", encoding="cp1252")
a=x.read()
words=a.split()
for i in words:
    if len(i) % 2 == 0:
        print(i)
    
=======
def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str

s="Consultadd Training"
print ("The original string  is : ",end="") 
print (s) 
  
print ("The reversed string(using loops) is : ",end="") 
print (reverse(s))
  
>>>>>>> 0c906ff... Add task6
