odd_numbers = 0
even_numbers = 0

while True:
    user_input = input("Enter a number or type 0 to stop: ")
    try:
        number = int(user_input)
    except ValueError:
        print("Please type valid data.")
        continue

    if number == 0:
        break

    if number % 2 == 1:
        odd_numbers += 1
    else:
        even_numbers += 1

print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)
