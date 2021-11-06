https://www.codewars.com/kata/5995ceb5d4280d07f6000822/train/python

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabetnums = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '10', 'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15', 'p': '16', 'q': '17', 'r': '18', 's': '19', 't': '20', 'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26'}
numsalpha = {}
for i in alphabetnums:
    numsalpha[alphabetnums[i]] = i
def AlphaNum_NumAlpha(string):
    conv = []
    inp = list(string)
    for ind,val in enumerate(inp):
        if val in alphabet:
            conv.append(alphabetnums[val])
        else:
            try:
                int(inp[ind-1])
                continue
            except:
                if not index.inp(val) == len(inp) - 1:
                    try:
                        int(inp[ind+1])
                        num = val + inp[ind+1]
                        conv.append(numsalpha[num])
                    except:
                        conv.append(numsalpha[val])
    return ''.join(conv)
print(AlphaNum_NumAlpha(input(f'test string\n> ')))