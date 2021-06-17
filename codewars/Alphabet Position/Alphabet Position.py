def alphabet_position(text):
    posit = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    text = text.lower()
    words = text.split()
    print(words)
    for word in words :
        for char in word :
            if char in alphabet : 
                ind = str(alphabet.find(char) + 1)
                posit.append(ind)
            else : continue
    delimiter = ' '
    sent = delimiter.join(posit)
    return sent
inp = input('')
print(alphabet_position(inp))