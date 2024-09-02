def multiplication_table(n, desirednum):
    for i in range(1, desirednum + 1):
        print(n, 'x', i, '=', n * i)


number = int(input("Enter a number: "))
desirednum = int(input("Enter the limit for the multiplication table: "))

# Calling the function with the desired number and limit
multiplication_table(number, desirednum)
