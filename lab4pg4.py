def fib(k):
    if k==1: return 0
    if k==2: return 1
    return fib (k-1)+fib(k-2)
t=int(input("Number of terms: "))
for i in range(1,t+1):
    print(fib(i),end=('  ' if i<t else '\n'))
