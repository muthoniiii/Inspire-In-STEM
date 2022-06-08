

import random

print("welcome to our password generator")
character=str("sheryl2004")
num_passwords = int(input("How many numbers do you want?"))
length=int(input("the password length?"))

print("\n here are your passwords")

for password in range (num_passwords):
    password=""

for c in range(length):
    password +=random.choice(character)
    print(password)




    #storing the user and the email(user accounts,user passwords)
