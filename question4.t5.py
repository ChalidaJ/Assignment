print('Enter correct userEmail and Password')
count=0
while count < 3:
    username = input('Enter username: ')
    password = input('Enter password: ')
    
    if password=='12345' and username=='Trylogin@gmail.com':
        print('Access granted')
        break
    else:
        print("Retype youe username or password")
        count += 1
        
print("Exceed the limits")
        

        