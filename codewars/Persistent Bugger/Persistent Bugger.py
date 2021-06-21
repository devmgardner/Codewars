global count
count = 1
def persistence(n):
    numl = list(str(n))
    if len(numl) == 1 : return 0
    total = 1
    for item in numl :
        total *= int(item)
        print(f'current total is {total}')
        print(f'length of current total is {len(str(total))}')
    print(f'final total is {total}')
    print(f'length of final total is {len(str(total))}')
    if len(str(total)) > 1 :
        global count; count += 1
        print(f'length of total({total}) is > 1, running again. current count is {count}')
        persistence(total)
    return count
    #while len(str(total)) > 1:
    #    persistence(total)
    #    count += 1
print(persistence(input('')))