
acc_bal = (int(input ( "what is your account balance?")))

if(int(acc_bal) > 100000 and int (acc_bal) < 200000):
    acc_bal = acc_bal-25000
    print("25000 has been  deducted from your account")
elif(int(acc_bal) > 500000 and int(acc_bal) < 1000000):
    acc_bal = acc_bal - (acc_bal*0.3)
    print("30 percent has been deducted from your account")
elif(int(acc_bal) > 1000000 ):
    acc_bal = acc_bal-15000
    print("15000 has been deducted from your account")




    
















