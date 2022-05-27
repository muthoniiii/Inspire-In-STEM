#usr/bin/python

number = input( "write the number")
factorial= 1
if  (int(number)) < 0:
    print("factorial of -ve numbers doesnt exist")
elif number== 0:
    print("factorial of 0 = 1")   
else:
    for i in range (1,(int(number))+1):
        factorial=factorial*i

print("Factorial of number is",factorial)