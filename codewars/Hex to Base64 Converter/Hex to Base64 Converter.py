hexalph = """!"#$%&'()*+,-./0123456789:'<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
def hexto64(hex_string) :
    n = list(hex_string.lower())
    n.reverse()
    nlist = []
    for char in n:
        ind = hexalph.index(char) + 33
        indlist = list(str(bin(ind)))
        indlist.pop(1)
        indlist = ''.join(indlist)
        nlist.append(indlist)
    nlist = ''.join(nlist)
    for i in range(2) :
        if not len(nlist) % 6 == 0 :
            nlist = list(nlist)
            nlist.append('00')
            nlist = ''.join(nlist)
    declist = []
    nlist = list(nlist)
    while len(nlist) > 0:
        word = nlist[:6]
        nlist = nlist[6:]
        declist.append(int(''.join(word)))
    finlist = []
    intlist = []
    for x in list(str(declist[0])) :
        intlist.append(int(x))
    print(f'intlist is {intlist}')
    for item in intlist:
        finlist.append(hexalph[item + 33])
    for i in range(3):
        if not len(finlist) % 4 == 0 :
            finlist.append('=')
    finlist = ''.join(finlist)
    return finlist
print(hexto64(input('')))