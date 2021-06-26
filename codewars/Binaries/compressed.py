import re
def code(strng):
    output = []
    chars = [bin(int(char)) for char in strng]
    binarychar = [char.replace('0b','') for char in chars]
    for char in binarychar :
        lenchar = len(char) - 1
        char = '1' + char
        while lenchar > 0 :
            char = '0' + char
            lenchar -= 1
        output.append(char)
    output = ''.join(output)
    return output
    
def decode(strng):
    output = []
    if re.search('[^01]', strng) : return ''
    while len(strng) > 0 :
        zero = re.search("^([0]*[1]{1})", strng)[0]
        strng = strng.replace(zero, '', 1)
        lenzero = len(zero)
        char = strng[:lenzero]; strng = strng[lenzero:]
        output.append(char)
    final = [str(int(item, 2)) for item in output]
    final = ''.join(final)
    return final