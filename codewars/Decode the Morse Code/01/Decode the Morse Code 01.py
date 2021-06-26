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
def decodeMorse(morse_code):
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
print(decodeMorse(input('')))
    