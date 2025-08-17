# text = str(input("Type a name:"))
# while True:
#     if text == "chupacabra":
#         print("You've successfully left the loop.")
#         break
#     else:
#         print("You are still in the loop.")
#         text = str(input("Type a name:"))   


# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = str(input("Type a word:"))
user_word = user_word.upper()

for letter in user_word:
    if letter in "AEIOU":
        continue
    print(letter, end=" \n")


    
    # Complete the body of the for loop.