num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
total = num1 + num2
print(f"The sum of {num1} and {num2} is {total}")
print(f"The difference between {num1} and {num2} is {num1 - num2}")
print(f"The product of {num1} and {num2} is {num1 * num2}")
if num2 != 0:
    print(f"The quotient of {num1} and {num2} is {num1/num2}")
else:
    print("Division by zero is not allowed.")