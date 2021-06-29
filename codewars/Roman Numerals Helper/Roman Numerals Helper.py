fname = 'Roman Numerals Helper-log.txt'
fhand = open(fname, 'w')
fhand.close()
fhand = open(fname, 'r+')
valid = {1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
class RomanNumerals():
    def to_roman(self):
        conv = []
        try:
            self = int(self)
        except:
            print('Invalid, quitting.')
            quit()
        fhand.write(f'starting value of self is {self}\n')
        for n in valid:
            fhand.write(f'n in valid is {n}\n')
            if self >= n:
                fhand.write(f'current self is {self}\n')
                x, y = divmod(self, n)
                self = y
                fhand.write(f'quotient is {x}, remainder is {y}. new self is {self}\n')
                for i in range(x):
                    conv.append(valid.get(n))
                    fhand.write(f'appending {valid.get(n)}\n')
        return ''.join(conv)
    

    def from_roman(self):
        #result = 0
        #newl = list(self)
        #for (ind, item) in enumerate(newl):
        #    print(f'currently checking item {ind}:{item}')
        #    if len(list(self)) == 1:
        #        result = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}.get(item)
        #        print(f'length is 1, result is {result}')
        #    #combo character
        #    elif not ind == (len(list(self)) - 1) and item + list(self)[ind+1] in {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}:
        #        print(f'index is not last in list, item and next item are in combo list')
        #        result += {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}.get(item + list(self)[ind+1])
        #    elif not ind == 0 and list(self)[ind-1] + item in {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}:
        #        print(f'prev item is not None, prev item and current item are in combo list, skipping')
        #        continue
        #    #last character, not combo
        #    elif ind == (len(list(self)) - 1) and not len(list(self)) == 1 and not list(self)[ind-1] + item in {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}:
        #        print(f'item is last in list, length of list is not 1, prev item and current item are not in combo list')
        #        result += {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}.get(item)
        #        continue
        #    elif ind != (len(list(self)) - 1) and {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}.get(item) >= {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}.get(list(self)[ind+1]):
        #        print(f'item is not last in list, item >= next item')
        #        result += {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}.get(item)
        #return result
        return sum([{'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}.get(item) if len(list(self)) == 1 else {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}.get(item + list(self)[ind+1]) if not ind == (len(list(self)) - 1) and item + list(self)[ind+1] in {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900} else 0 if not ind == 0 and list(self)[ind-1] + item in {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900} else {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}.get(item) if ind == (len(list(self)) - 1) and not len(list(self)) == 1 and not list(self)[ind-1] + item in {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900} else {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}.get(item) if ind != (len(list(self)) - 1) and {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}.get(item) >= {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}.get(list(self)[ind+1]) else None for (ind, item) in enumerate(list(self))])