import string
def pig_it(text):
    if len(text) == 0 : return ''
    return ''.join([word[1:] + word[0] + 'ay' if len(word) != 1 and list(word)[-1] not in string.punctuation else word + 'ay' if len(word) == 1 and word[0] not in string.punctuation else word[1:-1] + word[0] + 'ay' + word[-1] if len(word) > 0 and list(word)[-1] in string.punctuation else '' for word in text.split()])
print(pig_it(input('')))