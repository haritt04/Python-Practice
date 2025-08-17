import random

print("This is the Guess the Number game! Try to guess a number between 1 and 100.")
imagined_num = random.randint(1, 100)  # Generate a random number
print(f"the number is {imagined_num}")
guess = -1  # Initialize with an invalid number

while guess != imagined_num:
    try:
        guess = int(input("Guess the number: "))

        if guess < 1 or guess > 100:
            print("Please guess a number between 1 and 100.")
        elif guess > imagined_num:
            print("Too high! Try again.")
        elif guess < imagined_num:
            print("Too low! Try again.")
        else:
            print(f"Congrats! You guessed the number: {guess}")
    except ValueError:
        print("Invalid input! Please enter a valid number.")