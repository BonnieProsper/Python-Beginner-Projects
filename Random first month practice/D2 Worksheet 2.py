grade = float(input("Gimme ya grade: "))

if grade >= 90:
    print("Its an A!")
elif 80<=grade<=89:
    print("BBBBB")
elif 70<=grade<=79:
    print("C")
elif 60<=grade<=69:
    print("D")
else:
    print("Lowkey a failure")

grade=int(grade)
if grade%3==0:
    if grade%5==0:
        print("Both")
    else:
        print("Divisible by 3, not 5")
elif grade%5==0:
    print("divisible by 5 not 3")
else:
    print("neither")

password = input("Password: ")
for attempt in range(2):
    password = input("Password: ")
    if password == "python123":
        print("GRANTED!!")
        break
else:
    print("Ya done.")

'''
if password == "python123":
    print("GRANTEED!!")
else:
    password = input("Boo wrong. 1 more try: ")
    if password == "python123":
        print("Grantedddd")
    else:
        print("Ya done.")
'''

numbers = list(map(float, input("Gimme 3 nums: ").split()))
print(sorted(numbers))
print(min(numbers))
print(max(numbers))

    


