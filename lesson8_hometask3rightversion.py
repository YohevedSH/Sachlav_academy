text = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"
words = text.split()
new_words = []
for word in words:
    last = word[-1]
    if last == '.' or last == ',':
        word = word.replace(last, 'ing' + last)
    else: word = word + 'ing'
    new_words.append(word)
 

    
print(' '.join(new_words))
