def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero isnt allowed")
    return a / b
    
def exponent(a, b):
    return a**b

def remainder(a, b):
    return a%b

while True:
    op = input("Choose operation: ")
    if op == 'exit':
        break
    if op not in ['+', '-', '*', '/', '**', '%']:
        print("Invalid operation!")
        continue
    try:
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
        if op == '+':
            result = add(num1, num2)
        elif op == '-':
            result = subtract(num1, num2)
        elif op == '*':
            result = multiply(num1, num2)
        elif op == '/':
            result = divide(num1, num2)
        elif op == '**':
            result = exponent(num1, num2)
        elif op == '%':
            result = remainder(num1, num2)
        print(f"Result: {result:.2f}")
    except ValueError as e:
        print("Error:", e)

def ctof(c):
    return (c*9/5)+32

def ftoc(f):
    return (f-32)*5/9

while True:
    choice = input("1 for C→F, 2 for F→C, 'exit' to quit: ")
    if choice == 'exit':
        break
    if choice == '1':
        c = float(input("Enter temperature in °C: "))
        print(f"{c:.2f}°C = {ctof(c):.2f}°F")
    elif choice == '2':
        f = float(input("Enter temperature in °F: "))
        print(f"{f:.2f}°F = {ftoc(f):.2f}°C")
    else:
        print("Invalid choice.")


def checkprime(n):
    if n<=1:
        return False
    for i in range(2, int(n ** 0.5) +1):
        if n % i == 0:
            return False
    return True

def primesuntiln(n):
    for i in range(2, n+1):
        if checkprime(i):
            print(i, end=" ")
    # or use: return [i for i in range(2, n+1) if checkprime(i)]

num = int(input("Enter num: "))
if checkprime(num):
    print(f"{num} is prime")
else:
    print(f"{num} aint prime")
limit = int(input("Print all primes to: "))
primesuntiln(limit)

import random

options = ["rock", "paper", "scissors"]
playerscore = 0
compscore = 0

def decidewinner(player, computer):
    if player == computer:
        return "tie"
    elif ((player == "rock" and computer == "scissors") or
          (player == "paper" and computer == "rock") or
          (player == "scissors" and computer == "paper")):
        return "player"
    else:
        return "computer"

while True:
    player = input("Rock, paper, or scissors? ").lower()
    if player not in options:
        print("Invalid option")
        continue
    computer = random.choice(options)
    print(f"Computer chose {computer}")
    winner = decidewinner(player, computer)
    if winner == "player":
        playerscore += 1
        print("You win this round!")
    elif winner == "computer":
        compscore += 1
        print("Computer wins this round!")
    else:
        print("It's a tie!")
    print(f"Scores → You: {playerscore}, Computer: {compscore}")
    if input("Play again (y/n)? ").lower() != 'y':
        print("Thanks for playing!")
        break

def average(grades):
    return sum(grades)/len(grades)

def highest(grades):
    return max(grades)

def lowest(grades):
    return min(grades)

def grade_letter(score):
    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 70: return "C"
    elif score >= 60: return "D"
    else: return "F"

grades = []

while True:
    entry = input("Enter grades or done to finish: ")
    if entry.lower() == 'done':
        break
    try:
        grade = float(entry)
        grades.append(grade)
    except ValueError:
        print("Invalid input, try again.")
if grades:
    print(f"\nGrades: {grades}")
    print(f"Average: {average(grades):.2f}")
    print(f"Highest: {highest(grades)}")
    print(f"Lowest: {lowest(grades)}")
else:
    print("No grades entered")
