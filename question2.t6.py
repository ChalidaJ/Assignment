<<<<<<< HEAD
while True:
    try:
        name = input("Enter the file name: ")
        s=open(name, 'r')
        print(s.read())
        break
    except:
        print('File name is not correct')




=======
def multiple_element(n):
    return n*n
x=[1,2,3,4,5,6]
y=list(map(multiple_element, x))
print(y)

>>>>>>> 0c906ff... Add task6
