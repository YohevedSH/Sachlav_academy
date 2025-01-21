import re
words = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"
words = re.findall(r'\w+|\S', words)
text = [word + "ing" if word.isalpha() else word for word in words]
results = ' '.join(text)
print(results)