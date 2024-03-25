#CALCULATOR TASK

print("WELCOME TO MY CALCULATOR")
print("THE MENU OF OPERATIONS ARE:")
print("1.) Addition       (+)..")
print("2.) Subtraction    (-)..")
print("3.) Multiplication (*)..")
print("4.) Division       (/)..")
print("5.) Modulus        (%)..")
print("6.) Floor Division (//)..")

ch=int(input("Enter your choice here:"))
if ch == 1:
    a=int(input("Enter the first numnber:"))
    b=int(input("Enter the second number:"))
    print("The Sum is:",a+b)
    
elif ch == 2:
    a=int(input("Enter the first numnber:"))
    b=int(input("Enter the second number:")) 
    print("The Difference is:",a-b)
    
elif ch == 3:
    a=int(input("Enter the first numnber:"))
    b=int(input("Enter the second number:"))
    print("The product is:",a*b)
    
elif ch == 4:
    a=int(input("Enter the first numnber:"))
    b=int(input("Enter the second number:")) 
    print("The quotient is:",a/b)
    
elif ch == 5:
    a=int(input("Enter the first numnber:"))
    b=int(input("Enter the second number:"))
    print("The remainder is:",a%b)
    
elif ch == 6:
    a=int(input("Enter the first numnber:"))
    b=int(input("Enter the second number:"))
    print("The result is:",a//b)
    
