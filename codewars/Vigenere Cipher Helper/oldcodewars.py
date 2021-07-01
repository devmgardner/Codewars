ind = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
class VigenereCipher(object):
    table = [['ABCDEFGHIJKLMNOPQRSTUVWXYZ'],['BCDEFGHIJKLMNOPQRSTUVWXYZA'],['CDEFGHIJKLMNOPQRSTUVWXYZAB'],['DEFGHIJKLMNOPQRSTUVWXYZABC'],['EFGHIJKLMNOPQRSTUVWXYZABCD'],['FGHIJKLMNOPQRSTUVWXYZABCDE'],['GHIJKLMNOPQRSTUVWXYZABCDEF'],['HIJKLMNOPQRSTUVWXYZABCDEFG'],['IJKLMNOPQRSTUVWXYZABCDEFGH'],['JKLMNOPQRSTUVWXYZABCDEFGHI'],['KLMNOPQRSTUVWXYZABCDEFGHIJ'],['LMNOPQRSTUVWXYZABCDEFGHIJK'],['MNOPQRSTUVWXYZABCDEFGHIJKL'],['NOPQRSTUVWXYZABCDEFGHIJKLM'],['OPQRSTUVWXYZABCDEFGHIJKLMN'],['PQRSTUVWXYZABCDEFGHIJKLMNO'],['QRSTUVWXYZABCDEFGHIJKLMNOP'],['RSTUVWXYZABCDEFGHIJKLMNOPQ'],['STUVWXYZABCDEFGHIJKLMNOPQR'],['TUVWXYZABCDEFGHIJKLMNOPQRS'],['UVWXYZABCDEFGHIJKLMNOPQRST'],['VWXYZABCDEFGHIJKLMNOPQRSTU'],['WXYZABCDEFGHIJKLMNOPQRSTUV'],['XYZABCDEFGHIJKLMNOPQRSTUVW'],['YZABCDEFGHIJKLMNOPQRSTUVWX'],['ZABCDEFGHIJKLMNOPQRSTUVWXY']]
    def __init__(self, key, alphabet):
        global ind
        self.key = ''.join(str([ind.index(x.upper()) for x in key]))
        keyphrase=[]
        for i in range((len(str(self))%len(key))+1):keyphrase.append(key)
        lendiff=len(keyphrase)-len(str(self))
        if lendiff>0:keyphrase=keyphrase[:-lendiff]
        alphabet=[char.upper() for char in alphabet]


    
    def encode(self, text):
        global ind
        #sets up the index numbers of each character in self (column numbers)
        selfind = [ind.index(char.upper()) for char in list(str(text))]
        #sets up the index numbers of each character in key (row numbers)
        keyind = [ind.index(self.key.upper()) for char in list(self.key)]
        encoded = [table[keyind][selfind] for char in list(text) for char in list(self.key)]
        return ''.join(encoded)
    
    def decode(self, text):
        pass
