fname = 'Roman Numeral Decoderlog.txt'
fhand = open(fname, 'w')
fhand.close()
fhand = open(fname, 'r+')

inp = input('')
def solution(roman) :
    result = 0
    newl = list(roman)
    for (ind, item) in enumerate(newl) :
        if len(newl) == 1 : result = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}.get(item)
        #combo character
        elif not ind == (len(list(roman)) - 1) and item + list(roman)[ind+1] in {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900} :
            result += {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}.get(item + list(roman)[ind+1])
        elif not list(roman)[ind-1] is None and list(roman)[ind-1] + item in {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900} : continue
        #last character, not combo
        elif ind == (len(list(roman)) - 1) and not len(list(roman)) == 1 and not list(roman)[ind-1] + item in {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900} :
            result += {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}.get(item)
            continue
        elif ind != (len(list(roman)) - 1) and {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}.get(item) >= {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}.get(list(roman)[ind+1]) :
            result += {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}.get(item)
    return result
fhand.write(solution(inp))