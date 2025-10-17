num = int(input("Please enter number: "))
print(f"\nMultiplication Table for {num}")
print("-" * 25)
for i in range(1, 11):
    print(f"{num} x {i:2} = {num * i:3}")

numbers = list(map(float, input("Enter nums: ").split()))
count = len(numbers)
average = sum(numbers) / count
largest = max(numbers)
smallest = min(numbers)

above_avg = [n for n in numbers if n > average]

print(f"\nCount: {count}")
print(f"Average: {average:.2f}")
print(f"Largest: {largest}")
print(f"Smallest: {smallest}")
print(f"Nums above avg: {above_avg}")

sentence = input("Enter sentence: ")
print(f"\nAll caps: {sentence.upper()}")

words = sentence.split()
print(f"Word count: {len(words)}")

reversed_chars = sentence[::-1]
print(f"Reversed character: {reversed_chars}")

reversed_words = " ".join(words[::-1])
print(f"Reversed words: {reversed_words}")

import random
secret = random.randint(1, 20)
attempts = 0

print("Number between 1 and 20...")

while True:
    guess = int(input("Guess: "))
    attempts+=1
    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else: 
        print(f"Correct, in {attempts} tries")
        break
