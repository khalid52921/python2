#Task 1

# Ask the user to input the current temperature in Celsius
temperature = float(input("Enter the current temperature in Celsius: "))

# Determine and display the appropriate message
if temperature >= 30:
    print("It's a hot day. Stay hydrated!")
elif 20 <= temperature <= 29:
    print("It's a warm day. Enjoy the weather!")
elif 10 <= temperature <= 19:
    print("It's a cool day. Wear a jacket!")
else:
    print("It's a cold day. Stay warm!")



#Task 2

# Create a list of integers from 1 to 20
numbers = list(range(1, 21))

# Use a for loop to find numbers divisible by 3
divisible_by_3 = []  # This will store the results

for number in numbers:
    if number % 3 == 0:
        divisible_by_3.append(number)

# Print the numbers divisible by 3
print("Numbers divisible by 3:", divisible_by_3)
