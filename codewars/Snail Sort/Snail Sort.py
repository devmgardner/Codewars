#fname = 'Snail Sortlog.txt'
#fhand = open(fname, 'w')
#fhand.close()
#fhand = open(fname, 'r+')
snailist = []
def snail(snail_map):
    print(f'input is {snail_map}')
    if len(snail_map) == 1 :
        oneresult = []
        for item in snail_map[0] : oneresult.append(item)
        return oneresult
    if len(snail_map) == 2 :
        tworesult = []
        for item in snail_map[0] : tworesult.append(item)
        for item in reversed(snailmap[1]) : tworesult.append(item)
        return tworesult
    if len(snail_map) == 0 : return ''
    currentlist = snail_map
    def cycle(n) :
        for item in n[0] :
            print(f'cycling through first sublist, item is {item}')
            snailist.append(item)
            n[0].remove(item)
            if len(n[0]) == 0 : del n[0]
        templist = [item[len(item) - 1] for item in n]
        poplist = [item.pop(len(item) - 1) for item in n]
        for item in templist :
            snailist.append(item)
        templist.clear()
        poplist.clear()
        #revlist = [n[len(n) - 1]]
        for item in n :
            print(f'cycling through last in each list, item is {item}')
            subitem = item[len(item) - 1]
            snailist.append(subitem)
            item.remove(subitem)
        for item in reversed(n[len(n) - 1]) :
            print(f'cycling through last sublist, item is {item}')
            snailist.append(item)
            n[len(n) - 1].remove(item)
            if len(n[len(n) - 1]) == 0 : del n[len(n) - 1]
        return n
    cycle(currentlist)
    while not len(currentlist) == 0 : cycle(currentlist)
    return snailist