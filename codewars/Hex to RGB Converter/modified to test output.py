hexalph = '0123456789abcdef'
fname = 'HEXTORGB.txt'
fhand = open(fname, 'w')
fhand.close()
fhand = open(fname, 'r+')
def hex_string_to_RGB(hex_string): 
    def hextodec(n) :
        total = 0
        fhand.write(f'\n\n{n} IS CURRENT PAIR OF CHARACTERS\n')
        n = list(n.lower())
        n.reverse()
        print(f'after split and reverse, n is {n}\n')
        for ind, char in enumerate(n) :
            fhand.write(f'{ind},{char} is current index and character in input\n')
            fhand.write(f'{hexalph.index(char)} is index of character in hexalph list\n')
            fhand.write(f'{16 ** ind} is 16 ^ index\n')
            fhand.write(f'{(hexalph.index(char) * (16 ** ind))} is decimal form of hexadecimal input\n\n')
            total += (hexalph.index(char) * (16 ** ind))
        return total
    return {
        'r' : hextodec(hex_string[1:3]),
        'g' : hextodec(hex_string[3:5]),
        'b' : hextodec(hex_string[5:])
    }
print(hex_string_to_RGB(input('')))