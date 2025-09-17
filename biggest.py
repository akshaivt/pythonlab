a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    biggest = a
elif b >= a and b >= c:
    biggest = b
else:
    biggest = c

print("The biggest number is:", biggest)

