lst = list(map(int, input("Enter integers: ").split()))
result = [x for x in lst if x % 2 != 0]
print(result)

