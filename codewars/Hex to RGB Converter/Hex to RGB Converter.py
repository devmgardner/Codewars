hexalph = '0123456789abcdef'
def hex_string_to_RGB(hex_string): 
    def hextodec(n) :
        total = 0
        n = list(n.lower())
        n.reverse()
        print(f'after split and reverse, n is {n}')
        for ind, char in enumerate(n) :
            total += (hexalph.index(char) * (16 ** ind))
        return total
    return {
        'r' : hextodec(hex_string[1:3]),
        'g' : hextodec(hex_string[3:5]),
        'b' : hextodec(hex_string[5:])
    }
print(hex_string_to_RGB(input('')))