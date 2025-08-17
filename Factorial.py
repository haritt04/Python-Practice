while True:
    try:
        n = int(input("Enter a non-negative integer:"))
        if n < 0:
            print("Please enter a non-negative integer.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid non-negative integer.")
result = 1
for i in range(1, n + 1):
    result *= i 
print(f"The factorial of {n} is {result}")
