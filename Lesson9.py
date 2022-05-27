###################################
#        Dictionaries
#        Name:Sheryl Muthoni
#        Date:23/5/2021

#Initializing Dictionaries

from webbrowser import get


student={"Name":"sheryl","age":18,"Gender":"female","hobby":"swimming" }
#rint(student["hobby"])
student["ID number"]="23026124"
#print (student["ID number"])
student["movie"]="Stranger things"
#print(student)
#print(student["movie"])

#Initializing an empty Dictionary

#student ={}
student["favourite food"]="Chips"
student["colour"]="blue"
#print(student)

 #modifying values
#student["Name"]="chavelle"
#print(student["Name"])

#DELETING

del student["favourite food"]
#print(student)

#A collection of key value pairs
#syntax: dictionary ={"key":"value"}

color={'color':'red'}
vehicle={'type':'toyota' ,'plate number': 'KCD'}

#print(type(colors))
#print (type(names))# we usehe type method to

#Accessing values inside the data type (Dictionary)

print(vehicle["type"])#accessing the value of an element using a key
print(vehicle["plate number"],vehicle["type"])
print(type(vehicle))
name ={'name':'Sheryl  muthoni'}
phone_number ={'number':'0798414330'}
address={'address':'0414100'}
city={'city':'Nairobi'}

print(name["name"], phone_number["number"],address["address"],city["city"])
print(type(name))

person={'name':'sheryl','gender':'female',}
person['age']='18'
person['favourite color']='black'

#Accessing something from your dictionary
print(person)
print(person['name'],person['favourite color'])

#deletng something from your dictionary
#del person['favourite color']
#print(person)

#Looping over dictionaries
for key, value in person.items():
    print (f'{key}:{value}')


colors =["red","green","blue","yellow","purple"]

















