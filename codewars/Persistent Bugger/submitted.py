nlist = []
count = 1
def persistence(n):
    global count
    numl = list(str(n))
    if len(numl) == 1 : return 0
    total = 1
    for item in numl : total *= int(item)
    if len(str(total)) > 1 :
        count += 1
        nlist.append(total)
        persistence(total)
    if len(str(total)) == 1 :
        count = len(nlist) + 1
        del(nlist[:])
    return count