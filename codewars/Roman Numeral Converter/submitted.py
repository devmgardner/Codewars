def solution(roman) :
    nums = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,}
    valid = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
    result = 0
    newl = list(roman)
    for (ind, item) in enumerate(newl) :
        valueofchar = nums.get(item)
        lastindex = len(newl) - 1
        posofchar = ind
        if ind > 0 : prev = newl[ind - 1]
        if ind < (lastindex) : nex = newl[ind + 1]
        if not posofchar == 0 : prevchar = posofchar-1; prevval = nums.get(newl[prevchar])
        else : prevchar = prevval = None
        if not posofchar == lastindex : nextchar = posofchar+1; nextval = nums.get(newl[nextchar])
        else : nextchar = nextval = None
        if len(newl) == 1 : result = valueofchar
        elif not posofchar == lastindex and item + newl[nextchar] in valid : result += valid.get(item + newl[nextchar])
        elif not prevchar is None and newl[prevchar] + item in valid : continue
        elif posofchar == lastindex and not len(newl) == 1 and not newl[prevchar] + item in valid : result += valueofchar
        elif posofchar != lastindex and valueofchar >= nextval : result += valueofchar
    return result
print(solution(input('')))