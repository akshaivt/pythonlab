nums=list(map(int,input("enter integers: ").split()))
positives=[x for x in nums if x>0]
print ("Positives: ",positives)
N=int(input("Enter N: "))
squares=[i*i for i in range(1,N+1)]
print("squares 1...N:",squares)
word=input("enter a word: ")
vowels=[ch for ch in word if ch.lower() in 'aeiou']
print("vowels in word:", vowels)
ords=[ord(ch) for ch in word]
print("ordinals:",ords)
