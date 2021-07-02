import itertools
class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet
        self.finalalphtable = [self.alphabet[i:] + self.alphabet[:i] for i in range(len(self.alphabet))]
        self.key = ''.join([i for i in self.key])
    
    def encode(self, text):
        keyphrase = [i for i in self.key]
        self.text = text
        self.text = ''.join([i for i in self.text])
        while len(keyphrase) < len(self.text):
            keyphrase.append(self.key); keyphrase = ''.join(keyphrase); keyphrase = list(keyphrase)
        while len(keyphrase) > len(self.text): keyphrase = keyphrase[:-1]
        lendiff = len(keyphrase) - len(self.text)
        if lendiff > 0 : keyphrase = keyphrase[:-lendiff]
        keyphrase = [self.alphabet.index(i) if i in self.alphabet else None for i in keyphrase]
        return ''.join(list(itertools.chain(*[self.finalalphtable[k][self.alphabet.index(t)] if t in self.alphabet else t for t,k in zip(self.text, keyphrase)])))
    
    def decode(self, text):
        self.text = text
        keyphrase = [i for i in self.key]
        while len(keyphrase) < len(self.text):
            keyphrase.append(self.key); keyphrase = ''.join(keyphrase); keyphrase = list(keyphrase)
        while len(keyphrase) > len(self.text): keyphrase = keyphrase[:-1]
        lendiff = len(keyphrase) - len(self.text)
        if lendiff > 0 : keyphrase = keyphrase[:-lendiff]
        self.text = ''.join([i for i in self.text])
        keyphraseind = [self.alphabet.index(i) if i in self.alphabet else None for i in keyphrase]
        return ''.join([self.alphabet[self.finalalphtable[i].index(t)] if t in self.alphabet else t for t,k,i in zip(self.text, keyphrase, keyphraseind)])