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
