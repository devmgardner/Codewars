import re
def code(strng):
    cname = 'BinariesCodelog.txt'
    chand = open(cname, 'w')
    chand.close()
    chand = open(cname, 'r+')
    if strng == 'none' : return None
    output = []
    chand.write(f'chars in strng are: ')
    for char in strng :
        chand.write(f'{char}, ')
    chand.write('\n')
    chars = [bin(int(char)) for char in strng]
    chand.write(f'list of bin of int of chars in strng is:\n{chars}\n')
    binarychar = [char.replace('0b','') for char in chars]
    chand.write(f'list of chars with 0b removed is:\n{binarychar}\n')
    for char in binarychar :
        lenchar = len(char) - 1
        chand.write(f'(len of {char}) - 1 is {lenchar}\n')
        chand.write(f'{char} with leading 1 added is ')
        char = '1' + char
        chand.write(f'{char}\n')
        while lenchar > 0 :
            chand.write(f'(len of bin form of char) is > 1, adding leading 0 to turn {char} into ')
            char = '0' + char
            chand.write(f'{char}\n')
            lenchar -= 1
        output.append(char)
        chand.write(f'CURRENT OUTPUT LIST IS {output}\n')
    output = ''.join(output)
    chand.write(f'FINAL OUTPUT IS {output}\n#######')
    return output
    
def decode(strng):
    dname = 'BinariesDecodelog.txt'
    dhand = open(dname, 'w')
    dhand.close()
    dhand = open(dname, 'r+')
    output = []
    dhand.write(f'strng is {strng}\n')
    if re.search('[^01]', strng) : return ''
    while len(strng) > 0 :
        zero = re.search("^([0]*[1]{1})", strng)[0]
        strng = strng.replace(zero, '', 1)
        lenzero = len(zero)
        dhand.write(f'match is {zero} with length of {lenzero}\n')
        dhand.write(f'removal of match results in {strng}\n')
        char = strng[:lenzero]
        dhand.write(f'actual number is {char}\n')
        strng = strng[lenzero:]
        dhand.write(f'remaining strng after removal of number is {strng}\n')
        output.append(char)
    dhand.write(f'final list of matches is {output}\n')
    final = []
    for item in output :
        final.append(str(int(item, 2)))
        dhand.write(f'conversion of number is {int(item, 2)}\n')
    final = ''.join(final)
    dhand.write(f'final decode is {final}\n')
    return final
print(code(input('input to encode> ')))
print(decode(input('input to decode> ')))