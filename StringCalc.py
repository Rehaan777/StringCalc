from math import *

number1=float(input("Enter the first number: "))
number2=float(input("Enter your second number: "))
print("Your numbers are " + str(number1) + " and " + str(number2))
print("Enter yes/no")
confirm=input(("Confirmation: "))
if confirm==("yes"):
    operation=input(("Which operation do you want to perform on the given numbers? Enter addition/subtraction/multiplication/division/power "))
    if operation=="addition":
      print(number1+number2)
    elif operation=="subtraction":
      print(number1-number2)
    elif operation=="multiplication":
      print(number1*number2)
    elif operation=="division":
      print(number1/number2)
    elif operation=="power":
      print(pow(number1 , number2))
else:
    exit()