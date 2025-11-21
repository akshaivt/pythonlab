n=int(input("Enter a number: "))
temp=n
while temp>0:
    digit+temp%10
    sum+=digit**3
    temp//=10
    if sum==n:
        print("Armstrong number")
    else:
        print("Not an armstrong number")
