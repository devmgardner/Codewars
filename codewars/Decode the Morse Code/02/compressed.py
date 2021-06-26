import re
def decode_bits(bits):
    lowest = len(bits)
    bits = str(bits)
    if bits.startswith('0'): bits = re.sub('^(0+)','',bits)
    if bits.endswith('0'): bits = re.sub('(0+)$','',bits)
    seplist = []
    while len(bits) > 0 :
        seplist.append(re.match(f'^({bits[0]}+)',bits).group(1))
        bits = re.sub(f'^{bits[0]}+','',bits)
    for item in seplist :
        if len(item) < lowest : lowest = len(item)
    seplist = [item[:len(item) // lowest] for item in seplist]
    convertlist = []
    for item in seplist:
        if '1' in item:
            if len(item) == 1: convertlist.append('.')
            elif len(item) == 3: convertlist.append('-')
        if '0' in item:
            if len(item) == 1: continue
            if len(item) == 3: convertlist.append(' ')
            if len(item) == 7: convertlist.append('   ')
    convertlist = ''.join(convertlist)
    return convertlist
def decode_morse(morse_code):
    code = []
    morse_code = re.sub('\s{2,}','!',morse_code)
    words = morse_code.split(' ')
    if ' ' in words : words.remove(' ')
    while words[-1] == ' ' : del words[-1]
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
            else : code.append(MORSE_CODE[test])
        elif not '!' in word : code.append(MORSE_CODE[word])
    while code[-1] == '' or code[-1] == ' ' :
        code.pop(-1)
    code = ''.join(code)
    if len(code) >= 3 :
        if re.search('^[S]{1}\s*[O]{1}\s*[S]{1}', code) : re.sub('^[S]{1}\s*[O]{1}\s*[S]{1}','S O S', code)
    return code