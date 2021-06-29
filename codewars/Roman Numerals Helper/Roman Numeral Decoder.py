inp = input('')
def solution(self) :
    result = 0
    newl = list(self)
    for (ind, item) in enumerate(newl) :
        if len(list(self)) == 1 : result = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}.get(item)
        #combo character
        elif not ind == (len(list(self)) - 1) and item + list(self)[ind+1] in {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900} :
            result += {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}.get(item + list(self)[ind+1])
        elif not list(self)[ind-1] is None and list(self)[ind-1] + item in {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900} : continue
        #last character, not combo
        elif ind == (len(list(self)) - 1) and not len(list(self)) == 1 and not list(self)[ind-1] + item in {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900} :
            result += {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}.get(item)
            continue
        elif ind != (len(list(self)) - 1) and {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}.get(item) >= {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}.get(list(self)[ind+1]) :
            result += {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}.get(item)
    return result
    #result = sum([{'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}.get(item) if len(list(self)) == 1 else {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}.get(item + list(self)[ind+1]) if not ind == (len(list(self)) - 1) and item + list(self)[ind+1] in {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900} else 0 if not list(self)[ind-1] is None and list(self)[ind-1] + item in {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900} else {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}.get(item) if ind == (len(list(self)) - 1) and not len(list(self)) == 1 and not list(self)[ind-1] + item in {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900} else {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}.get(item) if ind != (len(list(self)) - 1) and {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}.get(item) >= {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}.get(list(self)[ind+1]) else None for (ind, item) in enumerate(list(self))])