def to_camel_case(text):
    #your code here
    sent = []
    if '-' in text :
        words = text.split('-')
    elif '_' in text :
        words = text.split('_')
    if words[0][0].isupper() == True :
        for word in words :
            word = word[:1].upper() + word[1:]
            sent.append(word)
    else : 
        sent.append(words[0])
        for word in words[1:] :
            word = word[:1].upper() + word[1:]
            sent.append(word)
    delimiter = ''
    sent = delimiter.join(sent)
    return sent
inp = input('')
print(to_camel_case(inp))