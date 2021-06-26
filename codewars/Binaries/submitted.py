#This code is incredibly messy and overcomplicated. It's just the way I do everything, and I'm trying to get better about it.
import re
def code(strng):
    #I have a custom snippet in VSCode that sets up python test files for me, that includes creating a log file called (pythonfilename)log.txt. This is so I can add write statements to every single operation to see if/when something goes wrong.
    cname = 'BinariesCodelog.txt'
    chand = open(cname, 'w')
    chand.close()
    chand = open(cname, 'r+')
    output = []
    chand.write(f'chars in strng are: ')
    for char in strng : chand.write(f'{char}, ')
    chand.write('\n')
    #The following line takes every character in the strng, converts it to an integer, then converts it to binary.
    chars = [bin(int(char)) for char in strng]
    chand.write(f'list of bin of int of chars in strng is:\n{chars}\n')
    #The line below removes python's added '0b' from the beginning of each string.
    binarychar = [char.replace('0b','') for char in chars]
    chand.write(f'list of chars with 0b removed is:\n{binarychar}\n')
    for char in binarychar :
        #The line below creates a variable for the length of the character - 1, to append this number of 0's to the beginning.
        lenchar = len(char) - 1
        chand.write(f'(len of {char}) - 1 is {lenchar}\n')
        chand.write(f'{char} with leading 1 added is ')
        #The line below, per the kata instructions, adds the leading '1' to every character regardless of length.
        char = '1' + char
        chand.write(f'{char}\n')
        while lenchar > 0 :
            chand.write(f'(len of bin form of char) is > 1, adding leading 0 to turn {char} into ')
            #For any character that is more than 1 bit, a number of '0's is added equal to the number of bits - 1.
            char = '0' + char
            chand.write(f'{char}\n')
            lenchar -= 1
        output.append(char)
        chand.write(f'CURRENT OUTPUT LIST IS {output}\n')
    #When final character has been processed, the list of characters is concatenated.
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
    #The following line checks to see if any character other than '0' or '1' is present in the input strng.
    if re.search('[^01]', strng) : return ''
    while len(strng) > 0 :
        #The following line matches zero or more '0's followed by exactly 1 '1'. This is the additional content added by the encoding seen above.
        zero = re.search("^([0]*[1]{1})", strng)[0]
        #The line below removes the match above from strng, but only the first match.
        strng = strng.replace(zero, '', 1)
        lenzero = len(zero)
        dhand.write(f'match is {zero} with length of {lenzero}\n')
        dhand.write(f'removal of match results in {strng}\n')
        #The line above and the lines below set the actual character value, and remove the character from the beginning of strng.
        char = strng[:lenzero]
        dhand.write(f'actual number is {char}\n')
        strng = strng[lenzero:]
        dhand.write(f'remaining strng after removal of number is {strng}\n')
        output.append(char)
    dhand.write(f'final list of matches is {output}\n')
    final = []
    #The simple loop below converts each actual character value into its decimal form and appends the string form of it to a list.
    for item in output :
        final.append(str(int(item, 2)))
        dhand.write(f'conversion of number is {int(item, 2)}\n')
    #The line below concatenates the list of string forms of decimal forms of parsed binary words into a single string.
    final = ''.join(final)
    dhand.write(f'final decode is {final}\n')
    return final
#print(code(input('input to encode> ')))
#print(decode(input('input to decode> ')))