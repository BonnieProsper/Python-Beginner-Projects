def factorial(n):
    if n==0 or n == 1:
        return 1
    result = 1
    for i in range(2, n+1):
        result *= i
    return result 

while True:
    try:
        num = int(input("Enter non-negative number for factorial: "))
        if num < 0:
            print("Error: Number must be non-negative.")
            continue
        print(f"{num}! = {factorial(num)}")
        break
    except ValueError:
        print("Invalid input. Enter an integer.")

sentence = input("Enter a sentence: ").lower().strip()
words = sentence.split() # splits on the spaces

word_count = {} # create empty dictionary

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word counts: ")
for word, count in word_count.items():
    print(f"{word}: {count}")

# OR 
# from collections import Counter
# word_count = Counter(words)
# print(word_count)

contacts = {}

while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View All Contacts")
    print("5. Quit")
    choice = input("Choose an option (from numbers above): ")
    if choice == '1':
        name = input("Enter name: ").title()
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print(f"{name} added.")
    elif choice == '2':
        name = input("Enter name to search: ").title()
        if name in contacts:
            print(f"{name}: {contacts[name]}")
        else:
            print("Contact not found.")
    elif choice == '3':
        name = input("Enter name to delete: ").title()
        if contacts.pop(name, None):
            print(f"{name} deleted.")
        else:
            print("Contact not found.")
    elif choice == '4':
        if contacts:
            print("All contacts: ")
            for name, phone in contacts.items:
                print(f"{name}: {phone}")
        else:
            print("No contacts saved.")
    elif choice == '5':
        print("Goodbye!")
        break
    else: 
        print("Invalid option.")


cart = {}

while True:
    print("\nShopping Cart Menu:")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. Checkout")
    choice = input("Choose an option (from numbers above): ")
    if choice == '1':
        item = input("Item name: ").title()
        try:
            price = float(input("Price: "))
            cart[item] = price
            print(f"{item} added for ${price:.2f}.")
        except ValueError:
            print("Invalid price.")
    elif choice == '2':
        item = input("Item name to remove: ").title()
        if cart.pop(item, None):
            print(f"{item} removed.")
        else:
            print("Item not in cart.")
    elif choice == '3':
        if cart:
            print("Your cart:")
            for item, price in cart.items():
                print(f"{item}: ${price:.2f}")
            total = sum(cart.values())
            print(f"Total: ${total:.2f}")
        else:
            print("Cart is empty.")
    elif choice == '4':
        if cart:
            total = sum(cart.values())
            print(f"Checkout complete. Total: ${total:.2f}")
        else:
            print("Cart is empty. Nothing to checkout.")
        break
    else:
        print("Invalid option.")

quiz = {
    "What's the captial of France?": "Paris",
    "2 + 2?": "4",
    "What is the colour of the sky?": "blue"
}
score = 0

for question, answer in quiz.items():
    user_answer = input(question + " ").strip().lower()
    if user_answer == answer.lower():
        print("Correct!")
        score+=1
    else:
        print(f"Wrong! Correct answer is {answer}.")

print(f"You got {score}/{len(quiz)} correct.")