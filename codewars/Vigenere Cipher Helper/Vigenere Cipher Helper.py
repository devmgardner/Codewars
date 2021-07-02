import itertools
class VigenereCipher(object):
    def __init__(self, key, alphabet):
        keyphrase = []
        self.key = key
        self.alphabet = alphabet
        self.finalalphtable = [self.alphabet[i:] + self.alphabet[:i] for i in range(len(self.alphabet))]
        self.key = ''.join([i for i in self.key])
    
    def encode(self, text):
        print(f'line 11 - starting encode method')
        keyphrase = [i for i in self.key]
        self.text = text
        self.text = ''.join([i for i in self.text])
        while len(keyphrase) < len(self.text):
            keyphrase.append(self.key); keyphrase = ''.join(keyphrase); keyphrase = list(keyphrase)
        while len(keyphrase) > len(self.text): keyphrase = keyphrase[:-1]
        print(f'line 18 - keyphrase is {keyphrase}')
        lendiff = len(keyphrase) - len(self.text)
        print(f'line 20 - lendiff is {lendiff}')
        if lendiff > 0 : keyphrase = keyphrase[:-lendiff]
        print(f'line 22 - keyphrase is {keyphrase}')
        keyphrase = [self.alphabet.index(i) if i in self.alphabet else None for i in keyphrase]
        print(f'line 24 - keyphrase is {keyphrase}')
        for t,k in zip(self.text, keyphrase):
            print(f'line 26 - t is """{t}""" and k is """{k}"""')
        for t,k in zip(self.text, keyphrase):
            print(f'line 28 - t is {t} and k is {k}')
        result = list(itertools.chain(*[self.finalalphtable[k][self.alphabet.index(t)] if t in self.alphabet else t for t,k in zip(self.text, keyphrase)]))
        result = ''.join(result)
        return result
    
    def decode(self, text):
        print(f'line 34 - starting decode method')
        self.text = text
        keyphrase = [i for i in self.key]
        print(f'line 37 - keyphrase is {keyphrase}')
        while len(keyphrase) < len(self.text):
            keyphrase.append(self.key); keyphrase = ''.join(keyphrase); keyphrase = list(keyphrase)
        while len(keyphrase) > len(self.text): keyphrase = keyphrase[:-1]
        print(f'line 41 - keyphrase is {keyphrase}')
        lendiff = len(keyphrase) - len(self.text)
        print(f'line 43 - lendiff is {lendiff}')
        if lendiff > 0 : keyphrase = keyphrase[:-lendiff]
        print(f'line 45 - keyphrase is {keyphrase}')
        self.text = ''.join([i for i in self.text])
        print(f'line 47 - text to decode is {self.text}')
        keyphraseind = [self.alphabet.index(i) if i in self.alphabet else None for i in keyphrase]
        print(f'line 49 - text to decode is {self.text}, keyphrase to use is {keyphrase}, keyphraseind is {keyphraseind}')
        testresults = []
        for t,k,i in zip(self.text, keyphrase, keyphraseind):
            print(f'line 52 - t is """{t}/{type(t)}""" and k is """{k}/{type(k)}""" and i is """{i}/{type(i)}"""')
            if t in self.alphabet:
                print(f'line 54 - located {t} in self.alphabet, continuing')
                print(f'line 55 - alphabet for this index is {self.finalalphtable[i]}')
                print(f'line 56 - index of current character in previously listed alphabet is {self.finalalphtable[i].index(t)}')
                print(f'line 57 - character at previously printed index in self.alphabet is {self.alphabet[self.finalalphtable[i].index(t)]}')
                testresults.append(self.alphabet[self.finalalphtable[i].index(t)])
            else:
                print(f'line 60 - {t} not located in self.alphabet, appending unchanged character')
                testresults.append(t)
        print(f'line 62 - final testresults list is:')
        print(testresults)
        result = [self.alphabet[self.finalalphtable[i].index(t)] if t in self.alphabet else t for t,k,i in zip(self.text, keyphrase, keyphraseind)]
        result = ''.join(result)
        return result
newitem = VigenereCipher(input('enter key> '), input('enter alphabet> '))
print(newitem.encode(input('enter input to encode> ')))