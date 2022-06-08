s = input("Enter the value : ")

reverse = s[:: -1]


if( s == reverse ):
    print("yes its a palindrome")
else:
    print("no its not a palindrome")    





s = input("Enter a string : ")#this are letters eg;abcde


#print(s[0:5])
#print(s[0:5:1])
#print(s[::])
#print(s[::-1])

revstr = (s[::-1])

if revstr == s:
    print("palindrome")
else:
    print("not a palindrome")


