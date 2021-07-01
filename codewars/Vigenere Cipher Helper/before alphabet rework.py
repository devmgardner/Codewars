import itertools
tableU = [[['A'],['B'],['C'],['D'],['E'],['F'],['G'],['H'],['I'],['J'],['K'],['L'],['M'],['N'],['O'],['P'],['Q'],['R'],['S'],['T'],['U'],['V'],['W'],['X'],['Y'],['Z']],[['B'],['C'],['D'],['E'],['F'],['G'],['H'],['I'],['J'],['K'],['L'],['M'],['N'],['O'],['P'],['Q'],['R'],['S'],['T'],['U'],['V'],['W'],['X'],['Y'],['Z'],['A']],[['C'],['D'],['E'],['F'],['G'],['H'],['I'],['J'],['K'],['L'],['M'],['N'],['O'],['P'],['Q'],['R'],['S'],['T'],['U'],['V'],['W'],['X'],['Y'],['Z'],['A'],['B']],[['D'],['E'],['F'],['G'],['H'],['I'],['J'],['K'],['L'],['M'],['N'],['O'],['P'],['Q'],['R'],['S'],['T'],['U'],['V'],['W'],['X'],['Y'],['Z'],['A'],['B'],['C']],[['E'],['F'],['G'],['H'],['I'],['J'],['K'],['L'],['M'],['N'],['O'],['P'],['Q'],['R'],['S'],['T'],['U'],['V'],['W'],['X'],['Y'],['Z'],['A'],['B'],['C'],['D']],[['F'],['G'],['H'],['I'],['J'],['K'],['L'],['M'],['N'],['O'],['P'],['Q'],['R'],['S'],['T'],['U'],['V'],['W'],['X'],['Y'],['Z'],['A'],['B'],['C'],['D'],['E']],[['G'],['H'],['I'],['J'],['K'],['L'],['M'],['N'],['O'],['P'],['Q'],['R'],['S'],['T'],['U'],['V'],['W'],['X'],['Y'],['Z'],['A'],['B'],['C'],['D'],['E'],['F']],[['H'],['I'],['J'],['K'],['L'],['M'],['N'],['O'],['P'],['Q'],['R'],['S'],['T'],['U'],['V'],['W'],['X'],['Y'],['Z'],['A'],['B'],['C'],['D'],['E'],['F'],['G']],[['I'],['J'],['K'],['L'],['M'],['N'],['O'],['P'],['Q'],['R'],['S'],['T'],['U'],['V'],['W'],['X'],['Y'],['Z'],['A'],['B'],['C'],['D'],['E'],['F'],['G'],['H']],[['J'],['K'],['L'],['M'],['N'],['O'],['P'],['Q'],['R'],['S'],['T'],['U'],['V'],['W'],['X'],['Y'],['Z'],['A'],['B'],['C'],['D'],['E'],['F'],['G'],['H'],['I']],[['K'],['L'],['M'],['N'],['O'],['P'],['Q'],['R'],['S'],['T'],['U'],['V'],['W'],['X'],['Y'],['Z'],['A'],['B'],['C'],['D'],['E'],['F'],['G'],['H'],['I'],['J']],[['L'],['M'],['N'],['O'],['P'],['Q'],['R'],['S'],['T'],['U'],['V'],['W'],['X'],['Y'],['Z'],['A'],['B'],['C'],['D'],['E'],['F'],['G'],['H'],['I'],['J'],['K']],[['M'],['N'],['O'],['P'],['Q'],['R'],['S'],['T'],['U'],['V'],['W'],['X'],['Y'],['Z'],['A'],['B'],['C'],['D'],['E'],['F'],['G'],['H'],['I'],['J'],['K'],['L']],[['N'],['O'],['P'],['Q'],['R'],['S'],['T'],['U'],['V'],['W'],['X'],['Y'],['Z'],['A'],['B'],['C'],['D'],['E'],['F'],['G'],['H'],['I'],['J'],['K'],['L'],['M']],[['O'],['P'],['Q'],['R'],['S'],['T'],['U'],['V'],['W'],['X'],['Y'],['Z'],['A'],['B'],['C'],['D'],['E'],['F'],['G'],['H'],['I'],['J'],['K'],['L'],['M'],['N']],[['P'],['Q'],['R'],['S'],['T'],['U'],['V'],['W'],['X'],['Y'],['Z'],['A'],['B'],['C'],['D'],['E'],['F'],['G'],['H'],['I'],['J'],['K'],['L'],['M'],['N'],['O']],[['Q'],['R'],['S'],['T'],['U'],['V'],['W'],['X'],['Y'],['Z'],['A'],['B'],['C'],['D'],['E'],['F'],['G'],['H'],['I'],['J'],['K'],['L'],['M'],['N'],['O'],['P']],[['R'],['S'],['T'],['U'],['V'],['W'],['X'],['Y'],['Z'],['A'],['B'],['C'],['D'],['E'],['F'],['G'],['H'],['I'],['J'],['K'],['L'],['M'],['N'],['O'],['P'],['Q']],[['S'],['T'],['U'],['V'],['W'],['X'],['Y'],['Z'],['A'],['B'],['C'],['D'],['E'],['F'],['G'],['H'],['I'],['J'],['K'],['L'],['M'],['N'],['O'],['P'],['Q'],['R']],[['T'],['U'],['V'],['W'],['X'],['Y'],['Z'],['A'],['B'],['C'],['D'],['E'],['F'],['G'],['H'],['I'],['J'],['K'],['L'],['M'],['N'],['O'],['P'],['Q'],['R'],['S']],[['U'],['V'],['W'],['X'],['Y'],['Z'],['A'],['B'],['C'],['D'],['E'],['F'],['G'],['H'],['I'],['J'],['K'],['L'],['M'],['N'],['O'],['P'],['Q'],['R'],['S'],['T']],[['V'],['W'],['X'],['Y'],['Z'],['A'],['B'],['C'],['D'],['E'],['F'],['G'],['H'],['I'],['J'],['K'],['L'],['M'],['N'],['O'],['P'],['Q'],['R'],['S'],['T'],['U']],[['W'],['X'],['Y'],['Z'],['A'],['B'],['C'],['D'],['E'],['F'],['G'],['H'],['I'],['J'],['K'],['L'],['M'],['N'],['O'],['P'],['Q'],['R'],['S'],['T'],['U'],['V']],[['X'],['Y'],['Z'],['A'],['B'],['C'],['D'],['E'],['F'],['G'],['H'],['I'],['J'],['K'],['L'],['M'],['N'],['O'],['P'],['Q'],['R'],['S'],['T'],['U'],['V'],['W']],[['Y'],['Z'],['A'],['B'],['C'],['D'],['E'],['F'],['G'],['H'],['I'],['J'],['K'],['L'],['M'],['N'],['O'],['P'],['Q'],['R'],['S'],['T'],['U'],['V'],['W'],['X']],[['Z'],['A'],['B'],['C'],['D'],['E'],['F'],['G'],['H'],['I'],['J'],['K'],['L'],['M'],['N'],['O'],['P'],['Q'],['R'],['S'],['T'],['U'],['V'],['W'],['X'],['Y']]]
tableL = [[['a'],['b'],['c'],['d'],['e'],['f'],['g'],['h'],['i'],['j'],['k'],['l'],['m'],['n'],['o'],['p'],['q'],['r'],['s'],['t'],['u'],['v'],['w'],['x'],['y'],['z']],[['b'],['c'],['d'],['e'],['f'],['g'],['h'],['i'],['j'],['k'],['l'],['m'],['n'],['o'],['p'],['q'],['r'],['s'],['t'],['u'],['v'],['w'],['x'],['y'],['z'],['a']],[['c'],['d'],['e'],['f'],['g'],['h'],['i'],['j'],['k'],['l'],['m'],['n'],['o'],['p'],['q'],['r'],['s'],['t'],['u'],['v'],['w'],['x'],['y'],['z'],['a'],['b']],[['d'],['e'],['f'],['g'],['h'],['i'],['j'],['k'],['l'],['m'],['n'],['o'],['p'],['q'],['r'],['s'],['t'],['u'],['v'],['w'],['x'],['y'],['z'],['a'],['b'],['c']],[['e'],['f'],['g'],['h'],['i'],['j'],['k'],['l'],['m'],['n'],['o'],['p'],['q'],['r'],['s'],['t'],['u'],['v'],['w'],['x'],['y'],['z'],['a'],['b'],['c'],['d']],[['f'],['g'],['h'],['i'],['j'],['k'],['l'],['m'],['n'],['o'],['p'],['q'],['r'],['s'],['t'],['u'],['v'],['w'],['x'],['y'],['z'],['a'],['b'],['c'],['d'],['e']],[['g'],['h'],['i'],['j'],['k'],['l'],['m'],['n'],['o'],['p'],['q'],['r'],['s'],['t'],['u'],['v'],['w'],['x'],['y'],['z'],['a'],['b'],['c'],['d'],['e'],['f']],[['h'],['i'],['j'],['k'],['l'],['m'],['n'],['o'],['p'],['q'],['r'],['s'],['t'],['u'],['v'],['w'],['x'],['y'],['z'],['a'],['b'],['c'],['d'],['e'],['f'],['g']],[['i'],['j'],['k'],['l'],['m'],['n'],['o'],['p'],['q'],['r'],['s'],['t'],['u'],['v'],['w'],['x'],['y'],['z'],['a'],['b'],['c'],['d'],['e'],['f'],['g'],['h']],[['j'],['k'],['l'],['m'],['n'],['o'],['p'],['q'],['r'],['s'],['t'],['u'],['v'],['w'],['x'],['y'],['z'],['a'],['b'],['c'],['d'],['e'],['f'],['g'],['h'],['i']],[['k'],['l'],['m'],['n'],['o'],['p'],['q'],['r'],['s'],['t'],['u'],['v'],['w'],['x'],['y'],['z'],['a'],['b'],['c'],['d'],['e'],['f'],['g'],['h'],['i'],['j']],[['l'],['m'],['n'],['o'],['p'],['q'],['r'],['s'],['t'],['u'],['v'],['w'],['x'],['y'],['z'],['a'],['b'],['c'],['d'],['e'],['f'],['g'],['h'],['i'],['j'],['k']],[['m'],['n'],['o'],['p'],['q'],['r'],['s'],['t'],['u'],['v'],['w'],['x'],['y'],['z'],['a'],['b'],['c'],['d'],['e'],['f'],['g'],['h'],['i'],['j'],['k'],['l']],[['n'],['o'],['p'],['q'],['r'],['s'],['t'],['u'],['v'],['w'],['x'],['y'],['z'],['a'],['b'],['c'],['d'],['e'],['f'],['g'],['h'],['i'],['j'],['k'],['l'],['m']],[['o'],['p'],['q'],['r'],['s'],['t'],['u'],['v'],['w'],['x'],['y'],['z'],['a'],['b'],['c'],['d'],['e'],['f'],['g'],['h'],['i'],['j'],['k'],['l'],['m'],['n']],[['p'],['q'],['r'],['s'],['t'],['u'],['v'],['w'],['x'],['y'],['z'],['a'],['b'],['c'],['d'],['e'],['f'],['g'],['h'],['i'],['j'],['k'],['l'],['m'],['n'],['o']],[['q'],['r'],['s'],['t'],['u'],['v'],['w'],['x'],['y'],['z'],['a'],['b'],['c'],['d'],['e'],['f'],['g'],['h'],['i'],['j'],['k'],['l'],['m'],['n'],['o'],['p']],[['r'],['s'],['t'],['u'],['v'],['w'],['x'],['y'],['z'],['a'],['b'],['c'],['d'],['e'],['f'],['g'],['h'],['i'],['j'],['k'],['l'],['m'],['n'],['o'],['p'],['q']],[['s'],['t'],['u'],['v'],['w'],['x'],['y'],['z'],['a'],['b'],['c'],['d'],['e'],['f'],['g'],['h'],['i'],['j'],['k'],['l'],['m'],['n'],['o'],['p'],['q'],['r']],[['t'],['u'],['v'],['w'],['x'],['y'],['z'],['a'],['b'],['c'],['d'],['e'],['f'],['g'],['h'],['i'],['j'],['k'],['l'],['m'],['n'],['o'],['p'],['q'],['r'],['s']],[['u'],['v'],['w'],['x'],['y'],['z'],['a'],['b'],['c'],['d'],['e'],['f'],['g'],['h'],['i'],['j'],['k'],['l'],['m'],['n'],['o'],['p'],['q'],['r'],['s'],['t']],[['v'],['w'],['x'],['y'],['z'],['a'],['b'],['c'],['d'],['e'],['f'],['g'],['h'],['i'],['j'],['k'],['l'],['m'],['n'],['o'],['p'],['q'],['r'],['s'],['t'],['u']],[['w'],['x'],['y'],['z'],['a'],['b'],['c'],['d'],['e'],['f'],['g'],['h'],['i'],['j'],['k'],['l'],['m'],['n'],['o'],['p'],['q'],['r'],['s'],['t'],['u'],['v']],[['x'],['y'],['z'],['a'],['b'],['c'],['d'],['e'],['f'],['g'],['h'],['i'],['j'],['k'],['l'],['m'],['n'],['o'],['p'],['q'],['r'],['s'],['t'],['u'],['v'],['w']],[['y'],['z'],['a'],['b'],['c'],['d'],['e'],['f'],['g'],['h'],['i'],['j'],['k'],['l'],['m'],['n'],['o'],['p'],['q'],['r'],['s'],['t'],['u'],['v'],['w'],['x']],[['z'],['a'],['b'],['c'],['d'],['e'],['f'],['g'],['h'],['i'],['j'],['k'],['l'],['m'],['n'],['o'],['p'],['q'],['r'],['s'],['t'],['u'],['v'],['w'],['x'],['y']]]
indU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
indL = 'abcdefghijklmnopqrstuvwxyz'
class VigenereCipher(object):
    def __init__(self, key, alphabet):
        keyphrase = []
        self.key = key
        print(f'line 10 - self.key is {self.key}')
        self.alphabet = alphabet
        print(f'line 12 - self.alphabet is {self.alphabet}')
        self.key = ''.join([i for i in self.key])
        print(f'line 14 - self.key after i.upper() list comp is {self.key}')
    
    def encode(self, text):
        keyphrase = [i for i in self.key]
        self.text = text
        self.text = ''.join([i for i in self.text])
        print(f'line 20 - self.text is {self.text}')
        print(f'line 21 - self.key is {self.key}')
        print(f'line 22 - len(self.key) is {len(self.key)}')
        print(f'line 23 - len(self.text) is {len(self.text)}')
        while len(keyphrase) < len(self.text):
            keyphrase.append(self.key); keyphrase = ''.join(keyphrase); keyphrase = list(keyphrase)
        while len(keyphrase) > len(self.text): keyphrase = keyphrase[:-1]
        #for i in range((len(self.text) % len(self.key)) +1) : keyphrase.append(self.key)
        print(f'line 28 - keyphrase is {keyphrase}')
        lendiff = len(keyphrase) - len(self.text)
        print(f'line 30 - lendiff is {lendiff}')
        if lendiff > 0 : keyphrase = keyphrase[:-lendiff]
        print(f'line 32 - keyphrase is {keyphrase}')
        keyphrase = [indU.index(i) if i in indU else indL.index(i) for i in keyphrase]
        print(f'line 34 - keyphrase is {keyphrase}')
        #result = []
        for t,k in zip(self.text, keyphrase):
            print(f't is """{t}""" and k is """{k}"""')
            if t in indU:
                print(tableU[indU.index(t)])
            elif t in indL:
                print(tableL[indL.index(t)])
        result = list(itertools.chain(*[tableU[k][indU.index(t)] if t in indU else tableL[k][indL.index(t)] for t,k in zip(self.text, keyphrase)]))
        result = ''.join(result)
        #for t,k in zip(self.text, keyphrase):
            #print(table[k])
            #result.append(table[k][ind.index(t)])
        return result
    
    def decode(self, text):
        self.text = text
        print(f'line 51 - self.text is {self.text}')
        keyphrase = [i for i in self.key]
        print(f'line 53 - keyphrase is {keyphrase}')
        self.text = ''.join([i for i in self.text])
        print(f'line 55 - self.text is {self.text}')
        keyphraseind = [indU.index(i) if i in indU else indL.index(i) for i in keyphrase]
        print(f'line 57 - keyphrase is {keyphrase}')
#        for item in keyphraseind:
#            if keyphrase[keyphraseind.index(item)] in indU:
#                print(f'line 54 - item in indU, item is {tableU[item]}')
#            elif keyphrase[keyphraseind.index(item)] in indL:
#                print(f'line 56 - item in indL, item is {tableL[item]}')
        result = []
        for t,k,i in zip(self.text, keyphrase, keyphraseind):
            print(f't is """{t}""" and k is """{k}""" and i is """{i}"""')
            if t in indU:
                print(indU[tableU[i].index([t])])
            elif t in indL:
                print(indL[tableL[i].index([t])])
        result = [indU[tableU[i].index([t])] if t in indU else indL[tableL[i].index([t])] for t,k,i in zip(self.text, keyphrase, keyphraseind)]
        print(f'line 71 - result is {result}')
        result = ''.join(result)
        return result
newitem = VigenereCipher(input('enter key> '), input('enter alphabet> '))
print(newitem.encode(input('enter input to encode> ')))