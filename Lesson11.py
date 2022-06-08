#usr/bin/python

#write a program that checks if numbers are divisible by 5 and 7

#input =input("enter a number:")
#x=int(input)
#if(int(x%5==0)) and (int(x%7==0)):
   # print("the number is divisible by 5 and 7")
#else:
   # print("the number is not divisble by 5 or 7")   

#challenges

#Program that customizes user input
##Challenge 1.
#print(" enter your name so as to customize the greetings")
#name=input("enter your name")

#print("hello",(name))

#Challenge 2
num=20
num+=num
print(num)

#Challenge 3




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