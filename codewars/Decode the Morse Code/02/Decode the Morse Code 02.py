import re
MORSE_CODE = {
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z', 
    '-----': '0',
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
    '.-.-.-': '.',
    '--..--': ',',
    '..--..': '?',
    '.----.': "'",
    '-.-.--': '!',
    '-..-.': '/',
    '-.--.': '(',
    '-.--.-': ')',
    '.-...': '&',
    '---...': ':',
    '-.-.-.': ';',
    '-...-': '=',
    '.-.-.': '+',
    '-....-': '-',
    '..--.-': '_',
    '.-..-.': '"',
    '...-..-': '$',
    '.--.-.': '@',
    '...---...': 'SOS'
}
def decode_bits(bits):
    lowest = len(bits)
    # ToDo: Accept 0's and 1's, return dots, dashes and spaces
    #return bits.replace('111', '-').replace('000', ' ').replace('1', '.').replace('0', '')
    bits = str(bits)
    if bits.startswith('0'):
        bits = re.sub('^(0+)','',bits)
        print('bits started with 0, 0s removed')
        print(f'bits is now {bits}')
    if bits.endswith('0'):
        bits = re.sub('(0+)$','',bits)
        print('bits ended with 0, 0s removed')
        print(f'bits is now {bits}')
    seplist = []
    while len(bits) > 0 :
        #first = bits[0]
        print(f'first is {bits[0]}')
        seplist.append(re.match(f'^({bits[0]}+)',bits).group(1))
        bits = re.sub(f'^{bits[0]}+','',bits)
        print(f'bits is {bits}')
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
    print(f'CONVERTLIST IS {convertlist}')
    return convertlist
#
#
#
#
#
def decode_morse(morse_code):
    print(f'input is {morse_code}')
    code = []
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    morse_code = re.sub('\s{2,}','!',morse_code)
    print(f'input after replacing multispaces with ! is {morse_code}')
    words = morse_code.split(' ')
    print(f'words is {words}')
    if ' ' in words :
        words.remove(' ')
    while words[-1] == ' ' :
        del words[-1]
    #morse_code = re.sub('\s{1}','a',morse_code)
    #morse_code = re.sub('!',' ',morse_code)
    #words = re.split('a', morse_code)
    #words = [item for word in words for item in word.split('!')]
    #print(words)
    #for ind, word in enumerate(words) :
    #    if word == '!' : words[ind] = ' '
    #word = re.findall('^(.+)', morse_code)
    #return morse_code.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).replace(' ', '')
    for word in words :
        print(f'word is {word}')
        if word == '' : continue
        if '!' in word :
            print(f'! found in {word}, splitting')
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
    print(f'list is currently {code}')
    while code[-1] == '' or code[-1] == ' ' :
        code.pop(-1)
        #for i in range(len(code) - 2) :
        #    if code[i] == 'S' and code[i + 1] == 'O' and code[i + 2] == 'S' :
        #        print(f'SOS found, replacing')
        #        code[i] = 'S O S'
        #        print(f'code[i] set to S O S: {code}')
        #        del code[i + 1]
        #        print(f'code[i + 1] deleted first time: {code}')
        #        del code[i + 1]
        #        print(f'code[i + 1] deleted second time: {code}')
    code = ''.join(code)
    if len(code) >= 3 :
        if re.search('^[S]{1}\s*[O]{1}\s*[S]{1}', code) :
            re.sub('^[S]{1}\s*[O]{1}\s*[S]{1}','S O S', code)
    return code
print(decode_morse(decode_bits(input(''))))
#print(decode_bits(input('')))