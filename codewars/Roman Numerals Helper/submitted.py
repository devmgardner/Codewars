valid = {1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
class RomanNumerals():
    def to_roman(self):
        conv=[]
        try:self=int(self)
        except:quit()
        for n in valid:
            if self>=n:
                x,y=divmod(self,n)
                self=y
                for i in range(x):conv.append(valid.get(n))
        return ''.join(conv)
    def from_roman(self):
        result=0
        return sum([{'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}.get(item) if len(list(self))==1 else {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}.get(item+list(self)[ind+1]) if not ind==(len(list(self))-1) and item+list(self)[ind+1] in {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900} else 0 if not ind==0 and list(self)[ind-1]+item in {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900} else {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}.get(item) if ind==(len(list(self))-1) and not len(list(self))==1 and not list(self)[ind-1]+item in {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900} else {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}.get(item) if ind!=(len(list(self))-1) and {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}.get(item)>={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}.get(list(self)[ind+1]) else None for (ind,item) in enumerate(list(self))])