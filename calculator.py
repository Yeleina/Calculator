print("Select an operation to perform:")

print("1 Add")
print("2 Subtract")
print("3 Divide")
print("4 Multiply")

operation = input("Enter Operation:")

if operation == "1" :
   num1 = int(input("Enter first number:"))
   num2 = int(input("Enter second number:"))
   print("The sum is" , num1 + num2)
elif operation =="2":
   num1 = int(input("Enter first number:"))
   num2 = int(input("Enter second number:"))
   print("The result is" ,num1 - num2)
elif operation == "3":
   num1 = int(input("Enter first number:"))
   num2 = int(input("Enter second number:"))
   print("The result is" , num1 / num2)
elif operation == "4":
   num1 = int(input("Enter first number:"))
   num2 = int(input("Enter second number:"))
   print("The result is" , num1 * num2)

else:
    print("Invalid Entry")