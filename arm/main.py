from armstrong import is_armstrong
start=int(input("Enter the starting number: "))
end=int(input("Enter the ending number: "))
print(f"armstrong numbers between{start} and {end} are:")
for num in range(start,end+1):
    if is_armstrong(num):
        print(num)
