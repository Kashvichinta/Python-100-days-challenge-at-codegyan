# if number is zero print like #Entered number is Zero"

#n = int(input())
#if n==0:
#    print("Entered number is zero")
#print("Program Executed")

# 2.check if number is zero or not
#approach 1
#num=int(input("Enter a number:"))
#if num !=0:
#   print("Number is not zero")
#else:
    #print("Number is zero")
#approach 2

#num=int(input("Enter a number:"))
#if num ==0:
    #print("Number is zero")
#else:
    #print("Number is not zero")
    
    
#check if number is even or odd
"""num= int (input("Enter a number:"))
if num%2==0:
    print("Number is EVEN")
else:
    print("Number is ODD")"""


num=int(input("Enter a number:"))
if num>-1 and num%2==0:
    print("Number is Positive Even")
elif num<0 and num%2==0:
    print("Number is Negative Even")
elif num>-1 and num%2!=0:
    print("Number is Positive Odd")
elif num<0 and num%2!=0:
    print("Number is Negative Odd")
else:
    print("Number is not mentioned in the above type")
print("Program Executed")    
    
