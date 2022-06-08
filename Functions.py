




#Definig a function/initializing a function
from tkinter.font import names
from unicodedata import name


def say_hello():
    print("Hello from JKUAT")
    x=4
    y=7
    z=x+y
    print(z)
say_hello()

def bark():
    print("Dogs bark ")
bark()

def chirps():
    print("A bird chirps")
chirps()    

def neighs():
    print("A horse neighs")
neighs()    



def add_numbers(g,h):
    sum_nums=g+h
    print("the sum of numbers",sum_nums)
add_numbers(40,50)
add_numbers(100,300)
add_numbers(10,30)
add_numbers(1,5)    

def prod_numbers(s,v):
    prod_numbers= s*v
    print("The multiple of numbers",prod_numbers)
prod_numbers(10,20)
prod_numbers(20,30)
prod_numbers(30,40)
prod_numbers(3,4)


# USING DEFAULT PARAMETERS

def print_name(name="Sheryl muthoni"):
    print(name)
print_name("max")


#RETURNING FROM A FUNCTION
def get_sum(num1,num2):
    sum_nums=num1+num2
    return sum_nums
print(get_sum(7,12))



#A function that gets the square of numbers

def powers(number,power):
    pow_num= number**power
    return pow_num
print(powers(6,4))

def get_full_name(f_name,s_name):
    full_name=f_name +" " + s_name
    return full_name
print(get_full_name("sheryl","muthoni"))


#RETURNING A DICTIONARY FROM A FUNCTION

def create_full_name(first_name,last_name):
    person = {'first':first_name , 'second': last_name}
    return person
student=create_full_name("Sheryl","muthoni")
print(student)


#USING A LIST IN A FUNCTION

def greet_friend(names):
    for name in names:
        msg ="hello"+ " " + name.title()+"!"
        print(msg)
friends=["Schantelle","Chelsea","sheryl","Nyamoita"] 
greet_friend(friends)   




    









