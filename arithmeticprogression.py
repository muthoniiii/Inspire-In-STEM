#usr/bin/python

#first 3 terms of an AP
#a first term,d is the common difference,n the number of terms

a = (int(input("enter the first term:")))
d = (int(input("enter the common difference:")))
n = (int(input("enter the number of terms:")))

for i in range (1,(int(n+1))):
    n_term = a +(i-1)*d
    print(n_term)

sn=(n_term/2)*(2*a + (n-1)*d)
print(sn)


    





