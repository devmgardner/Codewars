hda='0123456789abcdef';b64t="""ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"""
fn='log.txt';fh=open(fn,'w');fh.close();fh=open(fn,'r+')
def hextodec(s):
    l=[]
    h=list(s)
    while len(h)>0:
        hp=''.join(h[:2]);fh.write(f'Parsed hex pair {hp}\n')
        l.append(hp);h=h[2:]
    fh.write(f'List of parsed hex pairs is {l}\n')
    dl=[]
    for p in l:
        dcp=list(p.lower())
        fh.write(f'Lowercase pair list is {dcp}\n')
        dcp.reverse()
        fh.write(f'Reversed list is {dcp}\n')
        t=0
        for c in dcp:
            fh.write(f'{hda.index(c)} is index of character in hda list\n')
            fh.write(f'{dcp.index(c)} is index of character in input\n')
            fh.write(f'{16 ** dcp.index(c)} is 16 to the power of the index of the character in the input\n')
            fh.write(f'---Equation will be {hda.index(c)} * {16 ** dcp.index(c)}\n')
            t+=((hda.index(c))*(16**dcp.index(c)))
            fh.write(f'---Running total is {t}\n')
        t=str(t)
        fh.write(f'{t} is decimal conversion\n')
        dl.append(t)
    fh.write(f'{dl} is list of decimal conversions\n')
    bl=[]
    for n in dl :
        d=int(n)
        bc=f'{d:08b}'
        bc=list(bc)
        bc=''.join(bc)
        fh.write(f'{bc} is binary conversion of decimal\n')
        bl.append(bc)
    bl=''.join(bl)
    if not len(bl)%6==0:
        bl=list(bl)
        bl.append('00')
        bl=''.join(bl)
    if not len(bl)%6==0:
        bl=list(bl)
        bl.append('00')
        bl=''.join(bl)
    sb=[]
    while len(bl)>0:
        w=bl[:6]
        bl=bl[6:]
        w=''.join(w)
        fh.write(f'Parsed 6-bit word {w}\n')
        sb.append(w)
    fdl=[]
    for i in sb:
        fd=int(i,2)
        fd=str(fd)
        fh.write(f'{fd} is decimal conversion of 6-bit word {i}\n')
        fdl.append(fd)
    fl=[]
    for i in fdl:
        c=int(i)
        c=b64t[c]
        c=str(c)
        fh.write(f'{i} is decimal in list to convert using base64 table\n')
        fh.write(f'{c} is final character in base64 list using decimal conversion of 6-bit binary word as index\n')
        fl.append(c)
    fw=''.join(fl)
    fw=list(fw)
    if not len(fw)%4==0:fw.append('=')
    if not len(fw)%4==0:fw.append('=')
    if not len(fw)%4==0:fw.append('=')
    fw=''.join(fw)
    fh.write(f'{fw} is base64 conversion of {s}\n')
    return fw
print(hextodec(input('')))