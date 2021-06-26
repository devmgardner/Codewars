#I'm just going to say for the record, I know this is absolutely ridiculous and way too much code. There's no excuse or explanation, it's just messy. Function first, efficiency later.
import re
def decode_bits(bits):
    #This line sets the variable "lowest" to the length of the input so that it can be accurately changed later.
    lowest = len(bits)
    # ToDo: Accept 0's and 1's, return dots, dashes and spaces
    #return bits.replace('111', '-').replace('000', ' ').replace('1', '.').replace('0', '')
    bits = str(bits)
    #The two if statements below check if there are leading or trailing zeros and remove them
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
        print(f'first is {bits[0]}')
        #The line below takes the first character from the input, grabs the largest string of that character consecutively it can from the start of the string, and adds it to seplist.
        seplist.append(re.match(f'^({bits[0]}+)',bits).group(1))
        #This line removes the 'word' taken above from the input.
        bits = re.sub(f'^{bits[0]}+','',bits)
        print(f'bits is {bits}')
    #This simple for loop checks to see what the lowest length item is, that way the length of every item in the list can be divided by this value to account for differences in time units.
    for item in seplist :
        if len(item) < lowest : lowest = len(item)
    #The list comprehension below divides the length of each item in seplist by the lowest length, slices that many characters from each item, and sets the list to be those slices.
    seplist = [item[:len(item) // lowest] for item in seplist]
    convertlist = []
    for item in seplist:
        #The if statement below checks each 'word' to see if it is a dot or a dash based on its length.
        if '1' in item:
            if len(item) == 1: convertlist.append('.')
            elif len(item) == 3: convertlist.append('-')
        #This if statement checks each 'word' consisting of zeros. These and the statements above directly correlate to the international standard.
        if '0' in item:
            if len(item) == 1: continue
            if len(item) == 3: convertlist.append(' ')
            if len(item) == 7: convertlist.append('   ')
    #The statement below concatenates this all into one neat string to pass into the next function.
    convertlist = ''.join(convertlist)
    print(f'CONVERTLIST IS {convertlist}')
    return convertlist
#
#
#
#
#
#This is my exact function from the first kata in this series, only with a changed name to fit this kata.
def decode_morse(morse_code):
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