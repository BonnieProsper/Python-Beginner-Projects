grade = float(input("Give me your grade: "))

if grade >= 90:
    print("Its an A!")
elif 80<=grade<=89:
    print("Its a B!")
elif 70<=grade<=79:
    print("C")
elif 60<=grade<=69:
    print("D")
else:
    print("This is a failing grade")

grade=int(grade)
if grade%3==0:
    if grade%5==0:
        print("Divisible by both")
    else:
        print("Divisible by 3, not 5")
elif grade%5==0:
    print("divisible by 5 not 3")
else:
    print("Divisible by neither")

numbers = list(map(float, input("Give me 3 nums: ").split()))
print(sorted(numbers))
print(min(numbers))
print(max(numbers))

    


