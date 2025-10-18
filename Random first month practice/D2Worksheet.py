
num = int(input("Enter your number: "))
if num%2==0:
    if num%3==0:
        print(f"{num} is both even and a multiple of 3!")
    else:
        print(f"{num} is even but not a multiple of 3.")
else:
    if num%3==0:
        print(f"{num} is a multiple of 3 but not even.")
    else:
        print(f"{num} is neither")
              
num1, num2 = map(float, input("Enter 2 more numbers: ").split())
if num >= 0 and num1>=0 and num2 >= 0:
    print ("All positive.")
elif (num>=0 and num1>=0) or (num1>=0 and num2>=0) or (num>=0 and num2>=0):
    print("2 positive, 1 negative")
elif num>=0 or num1>=0 or num2>=0:
    print("1 positive")
else:
    print("None are positive")
print("Now to calculate triangles.")
tri_choice = input("Do you want me to (Y/N)")
if tri_choice.lower() == "y":
    triangle = 0.5*num1*num2
    print(f"Area: {triangle}")
else:
    print("Moving on.")
    line = list(map(int, input("Gimme some numbers, split using commas: ").split(',')))
    sum1 = 0
    for l in line:
        sum1+= l
    print(sum1)
    min1 = line[0]
    for l in line:
        if l < min1:
            min1 = l
    print(min1)
    max1 = line[0]
    for l in line:
        if l > max1:
            max1 = l
    print(max1)
        

            
