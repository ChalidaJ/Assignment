even_list=[6,8,10,14]
odd_list=[3,5,7]

for i in range(1,51) :
    x=int(input("Enter the number between 1 to 50:  "))
    if x % 2 == 0 :
        even_list.append(x)
        print("The new even_list is :  ", even_list)
        a=sum(even_list)
        print("The sum of the list is :  ", a)
        b=max(even_list)
        print("the max of the even+list is :  ", b)
        
    if x % 2 != 0 :
        odd_list.append(x)
        print("The new odd_list is : ", odd_list)
        c=sum(even_list)
        print("The sum of the list is :  ", c)
        d=max(even_list)
        print("the max of the even_list is :  ", d)
        
    
print("Number is too high")




