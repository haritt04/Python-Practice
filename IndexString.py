word = 'Programming'
print(word[0:7])


messgae = input("Write a letter :")
print("\nthe letter count is ", len(messgae) ,"." )

if messgae.islower():
    print("the letters are lower.")

elif messgae.isupper():
    print("The letters are upper.")
else:
    print("the letters are both mix.")


if "e" or "E" in messgae:
    print("\nthe messgae has", messgae.count('e'), "e.")
else:
    print("\nthe letter 'e' doesn't include.")