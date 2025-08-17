password = input("Enter your password: ")
attempts = 1

while (password != "Harry") and (attempts <= 3) :
        password =input("Try again :")
        attempts += 1

if  password == "Harry":
    print ("Login sucessfully.")
else:
    print("Too many Attempts.")
