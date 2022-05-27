
#rows = (int(input("enter number of rows")))
#for i in range(rows):#rows + 1
   # for j in range(i + 1):
        #print("*",end= " ")
    #print("\n")


#Full pyramids
k=0
rows = (int(input("enter rows")))
for i in range (1 , rows + 1):
    for space in range (1,(rows-i)+1):
        print(end=" ")
    while k!=(2*i-1):
        print("*",end =" ")
        k+=1
    k=0
    print()    
    



        

