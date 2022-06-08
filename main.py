


#usr/bin/python
#############################################################
############### name: sheryl muthoni#####################
################ Title: Importing data from one file to another###
############### Date : 06/06/2022##############################



import operations
from student import student
from teachers import Teachers


print(operations.add_numbers(3,4))
print(operations.sub_numbers(5,4))
print(operations.mult_numbers(3,10))
print(operations.div_numbers(9,4))



new_student = student("sheryl","swimming","2004")
student.greet_student()

new_teacher = Teachers("Mr.mwalya",int(7800),int(567),"Mathematics")
print(new_teacher.get_tsc_num)