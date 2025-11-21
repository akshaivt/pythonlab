import math
start, end = map(int, input("Enter range: ").split())
res = []
for num in range(start, end + 1):
    if all(int(d) % 2 == 0 for d in str(num)):
        if int(math.isqrt(num)) ** 2 == num:
            res.append(num)
print("Numbers:", res)
