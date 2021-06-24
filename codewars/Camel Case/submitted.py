import re
def to_camel_case(text):
    #your code here
    if len(text) == 0 : return ''
    sent = []
    words = re.split('[-_]', text)
    if words[0][0].isupper() == True :
        for word in words :
            word = word[:1].upper() + word[1:]
            sent.append(word)
    else : 
        sent.append(words[0])
        for word in words[1:] :
            word = word[:1].upper() + word[1:]
            sent.append(word)
    sent = ''.join(sent)
    return sent