##################################################3
############## sheryl muthoni ###################



#calling the function##

import math

a=int(input("Enter the coefficient of the first term:"))
b=int(input("Enter the coefficient of the second term:"))
c=int(input("Enter the constant:"))
w=math.sqrt(b**2 -4*a*c)

def find_roots(a,b,c):
    y_1 = ((-b + (w))/(2*a))
    y_2 = ((-b - (w))/ (2*a))
    print("The roots of the quadratic equation",y_1,y_2)

find_roots(a,b,c)
    

 
