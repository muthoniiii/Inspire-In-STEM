
#f = open("lesson.txt")

#creating a new file
#f = open("lesson1.txt",'x')

#reading in the file
#print(f.read())
#f.close()

#with open ("lesson1.txt",'w') as f:
    #f.write("Hello this is my new file \n")
    #f.write("Today is a good day ;)\n")
    #f.write("How is your day\n")
f =open("lesson1.txt")

f.readline()
print(f.readline())

f.seek()
print(f.seek())

f.tell()
print(f.tell())






