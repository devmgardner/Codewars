global count
count = 1
def persistence(n):
    numl = list(str(n))
    if len(numl) == 1 : return 0
    total = 1
    print(f'n is {n}')
    for item in numl :
        print(f'---\t{item} is current digit')
        total *= int(item)
        print(f'-----\t{total} is current total after multiplying by {item}')
        print(f'-----\t{len(str(total))} is length of current total')
    print(f'--\tfinal total is {total} with length of {len(str(total))}')
    if len(str(total)) > 1 :
        global count
        print(f'{count} is count after checking that length of current total is above 1')
        count += 1
        print(f'{count} is count after running count += 1')
        print(f'-------\tlength of total({total}) is > 1, running again. current count is {count}')
        persistence(total)
    return count
    #while len(str(total)) > 1:
    #    persistence(total)
    #    count += 1