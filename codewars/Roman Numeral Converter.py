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
    result = 0
    newl = list(roman)
    count = 0
    while count < len(newl)-1 :
        if nums.get(newl[count]) >= nums.get(newl[count+1]) :
            result += nums.get(newl[count])
            count += 1
        elif nums.get(newl[count]) < nums.get(newl[count+1]) :
            result += (nums.get(newl[count+1]) - nums.get(newl[count]))
            count += 1
    return result
print(solution(inp))