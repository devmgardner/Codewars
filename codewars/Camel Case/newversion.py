fname = 'camelcaselog.txt'
fhand = open(fname, 'w')
fhand.close()
fhand = open(fname, 'r+')
def to_camel_case(text):
    #your code here
    if len(text) == 0 : return ''
    sent = []
    if '-' in text :
        words = text.split('-')
        for word in words :
            fhand.write(f'{word}, ')
        fhand.write(f'\n')
    elif '_' in text :
        words = text.split('_')
        for word in words :
            fhand.write(f'{word}, ')
        fhand.write(f'\n')
    if words[0][0].isupper() == True :
        for word in words :
            word = word[:1].upper() + word[1:]
            fhand.write(f'{word}, ')
            sent.append(word)
        fhand.write(f'\n')
    else : 
        sent.append(words[0])
        for word in words[1:] :
            word = word[:1].upper() + word[1:]
            fhand.write(f'{word}, ')
            sent.append(word)
        fhand.write(f'\n')
    delimiter = ''
    sent = delimiter.join(sent)
    return sent
print(to_camel_case(input('')))