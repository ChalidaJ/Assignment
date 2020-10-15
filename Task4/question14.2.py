def a():
    try:
        f(x, 4)
    finally:
        print("after f")
        print("after f?")

a()

#
#after f
#after f?
#Traceback (most recent call last):
  #File "question14.2.py", line 8, in <module>
    #a()
  #File "question14.2.py", line 3, in a
    #f(x, 4)
#NameError: name 'f' is not defined