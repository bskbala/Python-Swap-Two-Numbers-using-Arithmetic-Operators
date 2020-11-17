# Python Swap Two Numbers using Arithmetic Operators #

a = float(input("Please Enter the Number a:"))
b = float (input("please Enter the Number b: "))

print("Before Swaping the  Numbers :a = {0}  and b={1}".format (a,b))
a=a +b
b =a-b
a=a-b

print("After  Swaping the  Numbers :a = {0}  and b={1}".format (a,b))