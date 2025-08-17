# income = float(input("Enter the annual income: "))

# if income < 85528:
# 	tax = income * 0.18 - 556.02
# elif income >= 85528:
#     tax = 14839.02 + (income - 85528) * 0.32
# if tax < 0:
#     tax = 0
# tax = round(tax, 0)
# print("The tax is:", tax, "thalers")


# As you surely know, due to some astronomical reasons, years may be leap or common. The former are 366 days long, while the latter are 365 days long.

# Since the introduction of the Gregorian calendar (in 1582), the following rule is used to determine the kind of year:

# if the year number isn't divisible by four, it's a common year;
# otherwise, if the year number isn't divisible by 100, it's a leap year;
# otherwise, if the year number isn't divisible by 400, it's a common year;
# otherwise, it's a leap year.
# Look at the code in the editor – it only reads a year number, and needs to be completed with the instructions implementing the test we've just described.
while True:
    try:
        year = int(input("Enter a year: "))
        if year < 1582:
            print("Not within the Gregorian calendar period")
        else:
            if year % 4 != 0:
                print("Common year")
            elif year % 100 != 0:
                print("Leap year")
            elif year % 400 != 0:
                print("Common year")
            else:
                print("Leap year")
        break
    except ValueError:
        print("Invalid input. Please enter a valid year.")
	