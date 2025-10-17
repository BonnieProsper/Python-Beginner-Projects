name = input("What is your name? ")
age = int(input("What is your age? "))
print(f"Hello, {name}! You are {age} years old - old as fuck lowkey.")
print(f"You'll be {age + 10} in 10 years.")

rand = int(input("Whats your favourite number? "))
if rand % 2 == 0:
    print("Its even (Its a girl!!!)")
else:
    print("Odd numbers are great too. Love an odd number")

temp_type = str(input("Give me a temperature, first tell me whether its celcius or fahrenheit (wierdo): "))
temp = float(input("Now the number pls: "))
if temp_type.lower() == "celsius":
    fahr_conv = temp * 9/5 + 32
    print(f"{fahr_conv:.2f}")
elif temp_type.lower() == "fahrenheit":
    cels_conv = (temp - 32) / (9/5)
    print(f"{cels_conv:.2f}")
else:
    print("uh... That aint celsius or fahrenheit buddy. Try again next time.")

width, length = map(float, input("Enter the width and length of your rectangle, seperated by a space: ").split())
print(f"The area is {width * length} cm^2")

principal, perc_rate, time_years = map(float, input("Gimme principal, rate(%) and years for this interest calc, all seperated by space: ").split())
interest = (principal * perc_rate * time_years) / 100
print(f"Here ya go, interest = {interest}")
