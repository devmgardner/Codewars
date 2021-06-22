hexalph = """                                 !"#$%&'()*+,-./0123456789:'<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
def hexto64(hex_string):
    n=list(hex_string.lower())
    n.reverse()
    nlist=[]
    for char in n:
        ind = hexalph.index(char)
        indlist = list(str(bin(ind)))
        indlist.pop(1)
        indlist = ''.join(indlist)
        nlist.append(indlist)
    nlist = ''.join(nlist)
    if not len(nlist)%6==0:nlist=list(nlist);nlist.append('00');nlist=''.join(nlist)
    if not len(nlist)%6==0:nlist=list(nlist);nlist.append('00');nlist=''.join(nlist)
    declist=[];nlist=list(nlist)
    while len(nlist)>0:
        word=nlist[:6];nlist=nlist[6:]
        declist.append(int(''.join(word)))
    finlist=[]
    for item in declist:
        finlist.append(hexalph[item])
    for i in range(3):
        if not len(finlist)%4==0:finlist.append('=')
    finlist = ''.join(finlist)
    return finlist
print(hexto64(input('')))