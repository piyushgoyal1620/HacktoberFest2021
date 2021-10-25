import math
op=input("Enter any one(+,-,*,/,sin,cos,tan,squareroot):")
if(op=="+"):
   a = int(input("enter first number:"))
   b = int(input("enter second number:"))
   print("Sum of your numbers is", a+b)
elif(op=="-"):
   a = int(input("enter first number:"))
   b = int(input("enter second number:"))
   print("substraction of your numbers is", a-b)
elif(op=="*"):
   a = int(input("enter first number:"))
   b = int(input("enter second number:"))
   print("Multiplication of your two numbers is", a*b)
elif(op=="/"):
   a = int(input("enter first number:"))
   b = int(input("enter second number:"))
   print("Quotient of your two numbers is", a/b)
elif(op=="sin"):
   x = int(input("> Input your number here: "))
   print(math.sin(x))
elif(op=="cos"):
   x = int(input("> Input your number here: "))
   print(math.cos(x))
elif(op=="tan"):
   x = int(input("> Input your number here: "))
   print(math.tan(x))
elif(op=="squareroot"):
   x = int(input(">Input your number here: ")) 
   print(math.sqrt(x))
else:
   print("Plese enter a valid operator") 