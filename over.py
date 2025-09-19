nums = list(map(int, input("Enter numbers: ").split()))
result=[x if x<=100 else "over" for x in nums]
print(result)
