text = input("Write a message :")
print("First character: ", text[0])
print("Last character: ", text[-1])
print("Middle character: ", text[int(len(text) / 2)])
print("Even index characters: ",text[0::2])
print("Odd index characters: ", text[1::2])
print("Reverse order: ", text[-1::-1])