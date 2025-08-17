import random

print("Welcome to the Guess Number Game.")
imagined_num = random.randint(1, 5)  # Generate a random number
print(imagined_num)
user_num = -1  # Initialize with an invalid number

while user_num != imagined_num:
    try:
        user_num = int(input("Guess the number between 1 to 5: "))
        if user_num < 1 or user_num > 5:
            print("Please guess a number between 1 and 5.")
        elif user_num == imagined_num:
            print(f"Congrats! You guessed the number: {user_num}")
        else:
            print("Wrong guess! Try again.")
    except ValueError:
        print("Invalid input! Please enter a number.")



