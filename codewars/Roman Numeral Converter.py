inp = input('')
def solution(roman) :
    nums = [
        ('I', 1, 1),
        ('V', 5, 2),
        ('X', 10, 3),
        ('L', 50, 4),
        ('C', 100, 5),
        ('D', 500, 6),
        ('M', 1000, 7),
    ]
    valid = {
        'IV' : 4,
        'IX' : 9,
        'XL' : 40,
        'CD' : 400,
        'CM' : 900
    }
    result = 0
    newl = list(roman)
    for item in newl :
        valueofchar = nums.get(item)
        lastindex = len(newl) - 1
        posofchar = newl.index(item)
        prevchar = posofchar-1
        nextchar = posofchar+1
        prevval = nums.get(newl[prevchar])
        if not posofchar == lastindex :
            nextval = nums.get(newl[nextchar])
        if len(newl) == 1 : result = valueofchar
        elif posofchar == lastindex and not len(newl) == 1 and not valueofchar > prevval : 
            result += valueofchar
        elif not posofchar == 0 and valueofchar > prevval : continue
        elif posofchar == lastindex and valueofchar > prevval : continue
        elif valueofchar >= nextval :
            result += valueofchar
        elif valueofchar < nextval :
            result += (nextval - valueofchar)
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