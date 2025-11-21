def simple_interest(p,t,r):return p*r*t/100
p=float(input("p: "))
t=float(input("t(yrs):"))
sen=input("Senior?(Y/N):").strip().lower()
r=12 if sen=='y' else 10
print("Rate: ",r,"%\n SI=",
      simple_interest(p,t,r))
