#for now, print a line to a file at every single opportunity to debug the whole program step by step
#number each function/thing that happens so debugging is easier
#all variable names should be long and descriptive until program works, then variable names can be shortened
#keep everything as spaced out as possible to be easier to read
#6afe16afbaf0e10a is current test string
########https://base64.guru/converter/encode/hex;
#
#above is place to easily test program
#
hexalph = """!"#$%&'()*+,-./0123456789:'<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
fname = 'testoutput.txt'
fhand = open(fname, 'w')
fhand.close()
fhand = open(fname, 'r+')
def hexto64(hex_string) :
    fhand.write(f'{hex_string} is input at beginning of function\n')
    hexlist = list(hex_string.lower())
    fhand.write(f'{hexlist} is lowercase list\n')
    hexlist.reverse()
    fhand.write(f'{hexlist} is reversed list\n')
    nlist = []
    for char in n :
        fhand.write(f'{char} is current char in n')