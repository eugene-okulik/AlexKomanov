import string

text = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero."

result = []
for word in text.split():
    if word[-1] in string.punctuation:
        stripped_word = word[:-1]
        punctuation = word[-1]
    else:
        stripped_word = word
        punctuation = ''

    new_word = stripped_word + 'ing' + punctuation
    result.append(new_word)

output = ' '.join(result)

print(output)
