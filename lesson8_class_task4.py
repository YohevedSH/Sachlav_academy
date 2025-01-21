word1 = input("First word").split()
word2 = input("Second word").split()
print("YES") if word1 == word2[::-1] else print("NO")