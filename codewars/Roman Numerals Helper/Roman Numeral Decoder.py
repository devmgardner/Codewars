fname = 'Roman Numeral Decoderlog.txt'
fhand = open(fname, 'w')
fhand.close()
fhand = open(fname, 'r+')

inp = input('')
def solution(roman) :
    nums = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    valid = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
    
    result = 0
    newl = list(roman)
    for (ind, item) in enumerate(newl) :
        fhand.write(f'char is {item}')
        fhand.write(f'nums.get(item) is {nums.get(item)}')
        if ind > 0 :
            prev = newl[ind - 1]
        if ind < (len(newl) - 1) :
            nex = newl[ind + 1]
        fhand.write(f'ind is {ind}')
        if not ind == 0 :
            prevchar = ind-1
            prevval = nums.get(newl[prevchar])
            fhand.write(f'prevchar is {newl[prevchar]}')
            fhand.write(f'prevval is {prevval}')
        else :
            prevchar = None
            prevval = None
        if not ind == (len(newl) - 1) :
            nextchar = ind+1
            nextval = nums.get(newl[nextchar])
            fhand.write(f'nextchar is {newl[nextchar]}')
            fhand.write(f'nextval is {nextval}')
        else :
            nextchar = None
            nextval = None
        if len(newl) == 1 : result = nums.get(item)
        elif not ind == (len(newl) - 1) and item + newl[nextchar] in valid :
            fhand.write('char and next are combo, adding')
            result += valid.get(item + newl[nextchar])
            fhand.write(f'current total is {result}')
        elif not prevchar is None and newl[prevchar] + item in valid : continue
        elif ind == (len(newl) - 1) and not len(newl) == 1 and not newl[prevchar] + item in valid :
            fhand.write('char is final character and is not combo with prevchar, adding')
            result += nums.get(item)
            fhand.write(f'current total is {result}')
            continue
        elif ind != (len(newl) - 1) and nums.get(item) >= nextval :
            fhand.write(f'ind is {ind}')
            fhand.write(f'(len(newl) - 1) is {(len(newl) - 1)}')
            fhand.write(f'nums.get(item) is {nums.get(item)}')
            fhand.write(f'nextval is {nextval}')
            fhand.write('char is higher than nextchar, adding')
            result += nums.get(item)
            fhand.write(f'current total is {result}')
    return result
#    while count < len(newl) :
#        if nums.get(newl[count]) >= nums.get(newl[count+1]) :
#            result += nums.get(newl[count])
#            count += 1
#        elif nums.get(newl[count]) < nums.get(newl[count+1]) :
#            result += (nums.get(newl[count+1]) - nums.get(newl[count]))
#            count += 1
#    return result
fhand.write(solution(inp))