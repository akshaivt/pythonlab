s = input("Enter string: ")
if s.endswith("ing"):
    s = s + "ly"
else:
    s = s + "ing"
print(s)

