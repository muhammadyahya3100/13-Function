def add(a,b):
  return a+b

def minus(a,b):
  return a-b
def multiply(a,b):
  return a*b
def divide(a,b):
   return a/b
choice = int(input("Ebter Your choice \n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n"))
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if choice == 1:
   print(num1,"+",num2,"=", add(num1,num2))
elif choice ==2:
   print(num1,"-",num2,"=",minus(num1,num2))
elif choice ==3:
   print(num1,"*",num2,"=",multiply(num1,num2))
elif choice ==4:
   print(num1,"/",num2,"=",divide(num1,num2))
else:
   print("Your choice is wrong!")
   