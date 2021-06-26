import re
def decoder(sequence):
    output=[]
    if re.search('[^01]',sequence):return ''
    while len(sequence)>0:
        zero=re.search('^(0*)1{1}',sequence).group(1)
        sequence=sequence.replace(zero,'',1)
        lenzero=len(zero)
        char=sequence[:lenzero+1];sequence=sequence[lenzero+1:]
        output.append(char)
    final=[]
    for item in output:final.append(int(item,2)-1)
    return final