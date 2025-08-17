secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
input_number = int(input("Enter your guess: "))

while input_number != secret_number:
        print("Ha ha! You're stuck in my loop!")
        input_number = int(input("Enter your guess: "))
        if input_number == secret_number:
            print("Well done, muggle! You are free now.")
        break

