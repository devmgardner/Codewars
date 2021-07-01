class VigenereCipher(object):
    table = [['ABCDEFGHIJKLMNOPQRSTUVWXYZ'],['BCDEFGHIJKLMNOPQRSTUVWXYZA'],['CDEFGHIJKLMNOPQRSTUVWXYZAB'],['DEFGHIJKLMNOPQRSTUVWXYZABC'],['EFGHIJKLMNOPQRSTUVWXYZABCD'],['FGHIJKLMNOPQRSTUVWXYZABCDE'],['GHIJKLMNOPQRSTUVWXYZABCDEF'],['HIJKLMNOPQRSTUVWXYZABCDEFG'],['IJKLMNOPQRSTUVWXYZABCDEFGH'],['JKLMNOPQRSTUVWXYZABCDEFGHI'],['KLMNOPQRSTUVWXYZABCDEFGHIJ'],['LMNOPQRSTUVWXYZABCDEFGHIJK'],['MNOPQRSTUVWXYZABCDEFGHIJKL'],['NOPQRSTUVWXYZABCDEFGHIJKLM'],['OPQRSTUVWXYZABCDEFGHIJKLMN'],['PQRSTUVWXYZABCDEFGHIJKLMNO'],['QRSTUVWXYZABCDEFGHIJKLMNOP'],['RSTUVWXYZABCDEFGHIJKLMNOPQ'],['STUVWXYZABCDEFGHIJKLMNOPQR'],['TUVWXYZABCDEFGHIJKLMNOPQRS'],['UVWXYZABCDEFGHIJKLMNOPQRST'],['VWXYZABCDEFGHIJKLMNOPQRSTU'],['WXYZABCDEFGHIJKLMNOPQRSTUV'],['XYZABCDEFGHIJKLMNOPQRSTUVW'],['YZABCDEFGHIJKLMNOPQRSTUVWX'],['ZABCDEFGHIJKLMNOPQRSTUVWXY']]
    ind = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    def __init__(self, key, alphabet):
        key = [ind.index(x.upper()) for x in key]
        keyphrase=[]
        for i in range((len(self) % len(key)) +1) : keyphrase.append(key)
        lendiff = len(keyphrase) - len(self)
        if lendiff > 0 : keyphrase = keyphrase[:-lendiff]
        alphabet = [char.upper() for char in alphabet]


    
    def encode(self, text):
        #sets up the index numbers of each character in self (column numbers)
        selfind = [ind.index(char.upper()) for char in list(self)]
        #sets up the index numbers of each character in key (row numbers)
        keyind = [ind.index(key.upper()) for char in list(self.key)]
        encoded = [table[keyind][selfind] for char in list(self) for char in list(key)]
        return ''.join(encoded)
    
    def decode(self, text):
        pass
