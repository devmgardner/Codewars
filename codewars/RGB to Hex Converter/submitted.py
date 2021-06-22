hexdict = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
def rgb(r, g, b):
    def hex(n) :
        n = int(n)
        if n > 255 : n = 255
        elif n < 0 : n = 0
        res1 = n // 16; rem1 = hexdict.get(n % 16)
        res2 = res1 // 16; rem2 = hexdict.get(res1 % 16)
        return rem2 + rem1
    hexval = hex(r) + hex(g) + hex(b)
    return hexval