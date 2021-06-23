#for now, print a line to a file at every single opportunity to debug the whole program step by step
#number each function/thing that happens so debugging is easier
#all variable names should be long and descriptive until program works, then variable names can be shortened
#keep everything as spaced out as possible to be easier to read
#6afe16afbaf0e10a is current test string
#av4Wr7rw4Qo= is final answer
########https://base64.guru/converter/encode/hex;
hexalph = """!"#$%&'()*+,-./0123456789:'<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
hexdecalph = '0123456789abcdef'
asciialph = """ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"""
fname = 'testoutput.txt'
fhand = open(fname, 'w')
fhand.close()
fhand = open(fname, 'r+')
def hexto64(hex_string) :
    #we first need to set up a list of pairs of the original hex string
    #each pair corresponds to an ascii character
    fhand.write(f'{hex_string} is the original hex-encoded string\n\n\n')
    hexstringlist = list(hex_string)
    hexcharacterlist = []
    #the while loop below iterates through each pair of characters in the list created by the input of the overall function
    #it then adds each of these pairs to another list, to be processed later
    while len(hexstringlist) > 2 :
        starthexpair = hexstringlist[:2]
        #starthexpair.reverse()
        hexpairstring = starthexpair[0] + starthexpair[1]
        hexcharacterlist.append(hexpairstring)
        hexstringlist = hexstringlist[2:]
    fhand.write(f'{hexcharacterlist} is the list of hexadecimal pairs after parsing\n')
    #now that we have a list of hex characters to process, we need to convert each one to its decimal counterpart
    #the function below converts a hexadecimal string into its decimal counterpart
    def hextodec(hexpair) :
        total = 0
        for ind, char in enumerate(hexpair) :
            fhand.write(f'{char} is current hexadecimal character to convert\n')
            total += (hexdecalph.index(char) * (16 ** ind))
        return total
    declist = []
    #the for loop below iterates through the list of hexadecimal strings and converts them to decimal
    #it then places the decimal numbers in a list to process later
    for item in hexcharacterlist :
        decimalversion = hextodec(str(item))
        declist.append(decimalversion)
    fhand.write(f'{declist} is the list of decimal numbers after being converted from hexadecimal\n')
    characterlist = []
    #each item in declist is an ascii character's decimal counterpart
    #the for loop below iterates through and converts the decimals to ascii characters
    #it does this by subtracting 33 and comparing to the hexalph list above
    for item in declist :
        fhand.write(f'{item} is the current decimal number to convert to ASCII\n')
        hexalphindex = item - 33
        fhand.write(f'{hexalphindex} is the index of the current decimal number - 33\n')
        character = hexalph[hexalphindex]
        characterlist.append(character)
    fhand.write(f'{characterlist} is the list of ASCII characters after processing\n')
    #we now have a list of ascii characters to turn into a string, and then convert to base64.
    asciistring = ''.join(characterlist)
    fhand.write(f'{asciistring} is the final ASCII string to be processed into base64\n\n\n')
    #the function below converts an ASCII string to base64
    def stringtobase64(asciistring) :
        fhand.write(f'{asciistring} is input at beginning of function\n')
        #The lines below were commented out because ASCII characters are actually case-sensitive, and as seen in the next set of comments, I misunderstood the instructions.
        #listofasciistringchars = list(asciistring.lower())
        #fhand.write(f'{listofasciistringchars} is lowercase list\n')
        #The lines below were commented out because I misunderstood. I built this function first, and added the hexadecimal functionality later.
        #I had already built the hexadecimal functionality for a different kata on codewars, so I brought it in and tweaked as necessary.
        #listofasciistringchars.reverse()
        #fhand.write(f'{listofasciistringchars} is reversed list\n')
        bit8list = []
        #The for loop below processes each character.
        for character in listofasciistringchars :
            fhand.write(f'{character} is current char in n\n')
            #The line below converts the character into its decimal representation.
            asciibinary = hexalph.index(character) + 33
            fhand.write(f'{asciibinary} is index + 33, for ASCII number\n')
            #The line below converts the decimal representation of the character into binary, converts that binary into a string, and then makes a list from that string.
            binarylist = list(str(bin(asciibinary)))
            fhand.write(f'{binarylist} is index, converted to binary, converted to a string, turned into a list\n')
            #Python adds a 'b' to binary representations, to denote that they are binary. The lines below remove the extraneous character and rejoin the numbers into a string.
            binarylist.pop(1)
            binarylist = ''.join(binarylist)
            fhand.write(f'{binarylist} is string version of 8bit binary of character, minus python added b\n')
            bit8list.append(binarylist)
        #The line below takes all of the binary representations of each ASCII character and converts them into one long string.
        bit8list = list(''.join(bit8list))
        #The loop below double-checks to make sure the string is divisible by 6, for further processing.
        for i in range(2) :
            if len(bit8list) % 6 != 0 : bit8list.append('0'); bit8list.append('0')
        fhand.write(f'{bit8list} is list of 8bit words after padding for 6 multiplicity\n')
        listof6bits = []
        #The while loop below processes every set of 6bit words in the list separately.
        while len(bit8list) > 6 :
            #The lines below pull 6 bits from the list for processing and remove those bits from the list.
            bit6word = bit8list[:6]
            fhand.write(f'{bit6word} is current 6bit word\n')
            bit8list = bit8list[6:]
            fhand.write(f'{bit8list} is list of 8bit words after removing 6bit word\n')
            #The lines below convert the 6bit word into a base2 integer, then turn that integer into a string, then add that string to a list for further processing.
            bit6word = str(int(''.join(bit6word), 2))
            fhand.write(f'{bit6word} is string form of integer form of 6bit word\n')
            listof6bits.append(bit6word)
        fhand.write(f'{listof6bits} is full list of 6bit words\n')
        finalcharacterlist = []
        #The loop below runs the final processing on each character.
        for word in listof6bits :
            wordinteger = int(word)
            fhand.write(f'{wordinteger} is integer form of word for asciialph index\n')
            finalcharacterlist.append(asciialph[wordinteger])
        #The for loop below ensures that the result is divisible by 4, by padding with '=' as necessary.
        for i in range(3) :
            if not len(finalcharacterlist) % 4 == 0 : finalcharacterlist.append('=')
        result = ''.join(finalcharacterlist)
        return result
    base64 = stringtobase64(asciistring)
    return base64
print(hexto64(input('')))