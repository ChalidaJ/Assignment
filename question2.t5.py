while True:
    try:
        name = input("Enter the file name: ")
        s=open(name, 'r')
        print(s.read())
        break
    except:
        print('File name is not correct')




