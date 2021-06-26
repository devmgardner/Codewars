import re
def decodeMorse(morse_code):
    code = []
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    morse_code = re.sub('\s{2,}','!',morse_code)
    words = morse_code.split(' ')
    if ' ' in words :
        words.remove(' ')
    while words[-1] == ' ' :
        del words[-1]
    for word in words :
        if word == '' : continue
        if '!' in word :
            word = word.split('!')
            while len(word) > 1 :
                test = word.pop(0)
                if test == '' : continue
                code.append(MORSE_CODE[test])
                code.append(' ')
            test = word.pop(0)
            if test == '' or test == ' ': continue
            else :
                code.append(MORSE_CODE[test])
        elif not '!' in word :
            code.append(MORSE_CODE[word])
    while code[-1] == '' or code[-1] == ' ' :
        code.pop(-1)
    code = ''.join(code)
    if len(code) >= 3 :
        if re.search('^[S]{1}\s*[O]{1}\s*[S]{1}', code) :
            re.sub('^[S]{1}\s*[O]{1}\s*[S]{1}','S O S', code)
    return code