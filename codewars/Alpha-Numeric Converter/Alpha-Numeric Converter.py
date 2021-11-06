#https://www.codewars.com/kata/5995ceb5d4280d07f6000822/train/python

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabetnums = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '10', 'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15', 'p': '16', 'q': '17', 'r': '18', 's': '19', 't': '20', 'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26'}
numsalpha = {}
for i in alphabetnums:
    numsalpha[alphabetnums[i]] = i
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
        if inp[0] in alphabet:
            conv.append(alphabetnums[inp[0]])
        else:
            conv.append(numsalpha[inp[0]])
    return ''.join(conv)
print(AlphaNum_NumAlpha(input(f'test string\n> ')))