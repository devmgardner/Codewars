#49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
#SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
########https://base64.guru/converter/encode/hex;
hexalph = """!"#$%&'()*+,-./0123456789:'<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
hexdecalph = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
finalascii = """ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"""
fname = 'NEWtestoutput.txt'
fhand = open(fname, 'w')
fhand.close()
fhand = open(fname, 'r+')
#
#
#
#start with hex_string
def hexto64(hex_string) :
    #convert hex_string to list (inputlist)
    fhand.write(f'{hex_string} is the original hex-encoded string\n\n\n')
    hexstringlist = list(hex_string)
    #initialize empty list (hexpairlist)
    hexpairlist = []
    #separate inputlist into pairs (hexpair)
    while len(hexstringlist) >= 2 :
        hexpair = hexstringlist[:2]
        fhand.write(f'{hexpair} IS CURRENT PAIR OF HEX CHARACTERS\n')
        #reverse hexpair, join into string, append to hexpairlist
        hexpair.reverse()
        hexpair = ''.join(hexpair)
        #fhand.write(f'{hexpair} is pair of hexadecimal characters to decode\n')
        hexpairlist.append(hexpair)
        hexstringlist = hexstringlist[2:]
    #fhand.write(f'{hexpairlist} is the list of hexadecimal pairs after parsing\n')
    #FUNCTION HEXTODEC
    def hextodec(inputpair) :
        #-pull from hextodec from hex>rgb converter, do not forget to remove reversal
        #-return the decimal form of each hex pair - 33 (for hexalph list)
        inputpair = list(inputpair.lower())
        fhand.write(f'{inputpair} is current input pair in lowercase\n\n\n')
        total = 0
        for ind, char in enumerate(inputpair) :
            fhand.write(f'{char} is current hexadecimal character to convert\n')
            total += (hexdecalph.index(char) + (16 ** ind))
        return total
    #initialize empty list (asciicharacterlist)
    asciicharacterlist = []
    #initialize empty list (listcharacterdecimal)
    listcharacterdecimal = []
    #for each pair in hexpairlist:
    fhand.write(f'{hexpairlist} IS CURRENT LIST OF HEX PAIRS\n')
    for item in hexpairlist :
        #run pair through hextodec function, set to variable characterdecimal
        characterdecimal = hextodec(item)
        #append str version of characterdecimal to listcharacterdecimal
        listcharacterdecimal.append(str(characterdecimal))
    fhand.write(f'{listcharacterdecimal} is list of decimal numbers after being converted from hexadecimal\n')
    #use characterdecimal as index for hexalph list, append each asciicharacter to asciicharacterlist
    for item in listcharacterdecimal :
        asciicharacter = hexalph[int(item) - 33]
        asciicharacterlist.append(asciicharacter)
    #print asciicharacterlist
    fhand.write(f'{asciicharacterlist} is list of ASCII characters after processiong\n')
    #initialize empty list (binarylist)
    binarylist = []
    #for each number in listcharacterdecimal:
    for number in listcharacterdecimal :
        #turn the number into an integer again
        num = int(number)
        #convert that integer to binary, the binary to a list, remove the 'b' python adds (list[1]), then join back to a string
        binaryint = list(str(bin(num)))
        binaryint.pop(1)
        binaryint = ''.join(binaryint)
        #append string to binarylist
        binarylist.append(binaryint)
    #convert binarylist into one long string
    binarylist = ''.join(binarylist)
    fhand.write(f'{binarylist} is binary of words\n')
    #if length of binarylist isn't divisible by 6:
    if not len(binarylist) % 6 == 0 :
        #convert string into list, append 00, convert back to string, check again
        binarylist = list(binarylist)
        binarylist.append('00')
        binarylist = ''.join(binarylist)
    if not len(binarylist) % 6 == 0 :
        #convert string into list, append 00, convert back to string, check again
        binarylist = list(binarylist)
        binarylist.append('00')
        binarylist = ''.join(binarylist)
    #convert binarylist back into a list
    binarylist = list(binarylist)
    fhand.write(f'{binarylist} is binarylist after padding if necessary\n')
    #initialize empty list (listfinaldecimal)
    listfinaldecimal = []
    #while the length of the binarylist is greater than 6:
    while len(binarylist) >= 6 :
        #set sixbitword to be the first 6 characters in the list as a string
        sixbitword = binarylist[:6]
        #remove first 6 characters from binarylist
        binarylist = binarylist[6:]
        sixbitword = ''.join(sixbitword)
        fhand.write(f'{sixbitword} is current 6bit word\n')
        #join sixbitword into a string, then get the base2 integer form of it, then convert it to a string again, then append it to listfinaldecimal
        sixbitword = int(sixbitword, 2)
        fhand.write(f'{sixbitword} is base2 integer of sixbitword\n')
        sixbitword = str(sixbitword)
        listfinaldecimal.append(sixbitword)
    #initialize empty list (listfinalascii)
    listfinalascii = []
    fhand.write(f'{listfinaldecimal} is list of final decimal numbers for ASCII conversion\n')
    #for each finaldecimal in listfinaldecimal:
    for finaldec in listfinaldecimal :
        #convert finaldecimal to an integer
        finaldec = int(finaldec)
        #get the finaldecimal index from the finalascii list
        finalchar = finalascii[finaldec]
        #append to listfinalascii
        listfinalascii.append(finalchar)
    #join listfinalascii into one long string
    result = ''.join(listfinalascii)
    #if listfinalascii isn't divisible by 4, convert it to a list, append =, convert back to string, repeat until divisible by 4
    for i in range(3) :
        if len(result) % 4 != 0 :
            result = list(result)
            result.append('=')
            result = ''.join(result)
    return result
print(hexto64(input('')))