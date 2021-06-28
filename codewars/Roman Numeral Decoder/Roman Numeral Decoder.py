inp = input('')
def solution(roman) :
    nums = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    valid = {
        'IV' : 4,
        'IX' : 9,
        'XL' : 40,
        'XC' : 90,
        'CD' : 400,
        'CM' : 900
    }
    res = [nums[item] if not nums]
    result = 0
    newl = list(roman)
    for (ind, item) in enumerate(newl) :
        valueofchar = nums.get(item)
        print(f'char is {item}')
        print(f'valueofchar is {valueofchar}')
        lastindex = len(newl) - 1
        posofchar = ind
        if ind > 0 :
            prev = newl[ind - 1]
        if ind < (lastindex) :
            nex = newl[ind + 1]
        print(f'posofchar is {posofchar}')
        if not posofchar == 0 :
            prevchar = posofchar-1
            prevval = nums.get(newl[prevchar])
            print(f'prevchar is {newl[prevchar]}')
            print(f'prevval is {prevval}')
        else :
            prevchar = None
            prevval = None
        if not posofchar == lastindex :
            nextchar = posofchar+1
            nextval = nums.get(newl[nextchar])
            print(f'nextchar is {newl[nextchar]}')
            print(f'nextval is {nextval}')
        else :
            nextchar = None
            nextval = None
        if len(newl) == 1 : result = valueofchar
        elif not posofchar == lastindex and item + newl[nextchar] in valid :
            print('char and next are combo, adding')
            result += valid.get(item + newl[nextchar])
            print(f'current total is {result}')
        elif not prevchar is None and newl[prevchar] + item in valid : continue
        elif posofchar == lastindex and not len(newl) == 1 and not newl[prevchar] + item in valid :
            print('char is final character and is not combo with prevchar, adding')
            result += valueofchar
            print(f'current total is {result}')
            continue
        #elif posofchar == lastindex and not len(newl) == 1 and not valueofchar > prevval : 
            #result += valueofchar
        #elif not posofchar == 0 and valueofchar > prevval : continue
        #elif posofchar == lastindex and valueofchar > prevval : continue
        elif posofchar != lastindex and valueofchar >= nextval :
            print(f'posofchar is {posofchar}')
            print(f'lastindex is {lastindex}')
            print(f'valueofchar is {valueofchar}')
            print(f'nextval is {nextval}')
            print('char is higher than nextchar, adding')
            result += valueofchar
            print(f'current total is {result}')
        #elif valueofchar < nextval :
            #result += (nextval - valueofchar)
    return result
#    while count < len(newl) :
#        if nums.get(newl[count]) >= nums.get(newl[count+1]) :
#            result += nums.get(newl[count])
#            count += 1
#        elif nums.get(newl[count]) < nums.get(newl[count+1]) :
#            result += (nums.get(newl[count+1]) - nums.get(newl[count]))
#            count += 1
#    return result
print(solution(inp))