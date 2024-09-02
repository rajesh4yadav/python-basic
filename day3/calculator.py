print("          welcome to calculator  ")



print("Which calculation do you like ko perform")
print('    1.Addition')
print('    2.Subtaction')
print('    3.Multiplication')
print('    4.Division')
print('    5.square')

operation =input()

if operation== "1":
    a=int(input("Enter the first number "))
    b=int(input("Enter the second Number "))
    print("The sum Is " , (a+b) )
    
    
elif operation=="2":
    a=int(input("Enter the first number  "))
    b=int(input("Enter the second Number "))
    print("The subtraction Is " , (a-b) )
    
elif operation=="3":
    a=int(input("Enter the first number "))
    b=int(input("Enter the second Number "))
    print("The multiplication Is " , (a*b) )
    
elif operation=="4":
    a=int(input("Enter the first number "))
    b=int(input("Enter the second Number "))
    print("The division Is " , (a/b) )
    
elif operation =="5":
    a=int(input("Enter the  number "))
    print("The square of the given number is", (a*a))
    
else:
    print("invalid input")