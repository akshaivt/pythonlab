words = input("Enter words (space separated): ").split()
if words:
    max_len = max(len(w) for w in words)
    print("Length of longest word:", max_len)
else:
    print("No words entered.")

