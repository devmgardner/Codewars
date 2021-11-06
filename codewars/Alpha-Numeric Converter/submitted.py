numsalpha = {}
for i in alphabetnums: numsalpha[alphabetnums[i]] = i
def AlphaNum_NumAlpha(string):
    conv = []
    inp = list(str(string))
    while len(inp) > 1:
        if inp[0] in alphabet:
            conv.append(alphabetnums[inp[0]])
            del inp[0]
        elif not inp[0] in alphabet:
            if not inp[1] in alphabet:
                num = inp[0] + inp[1]
                conv.append(numsalpha[num])
                del inp[:2]
            elif inp[1] in alphabet:
                conv.append(numsalpha[inp[0]])
                del inp[0]
    if len(inp) == 1:
        if inp[0] in alphabet: conv.append(alphabetnums[inp[0]])
        else: conv.append(numsalpha[inp[0]])
    return ''.join(conv)