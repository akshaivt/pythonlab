def sum_vars(*nums):
    """Return sum of any numbers of integer arguments."""
    return sum(nums)
s=input("Enter integers (spaces seperated ):").strip()
if s: 
    nums=list(map(int,s.split()))
    print("sum=",sum_vars(*nums))
else:
    print("No numbers entered.")
