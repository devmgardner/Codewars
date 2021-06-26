#fname = 'Snail Sortlog.txt'
#fhand = open(fname, 'w')
#fhand.close()
#fhand = open(fname, 'r+')
snailist = []
def snail(snail_map):
    snailist = []
    print(f'input is {snail_map}')
    if len(snail_map) == 1 :
        oneresult = []
        for item in snail_map[0] : oneresult.append(item)
        return oneresult
    if len(snail_map) == 2 :
        tworesult = []
        for item in snail_map[0] : tworesult.append(item)
        for item in reversed(snail_map[1]) : tworesult.append(item)
        return tworesult
    if len(snail_map) == 0 : return ''
    currentlist = snail_map
    def cycle(n) :
        for item in n[0] :
            #print(f'cycling through first sublist, item is {item}')
            snailist.append(item)
            #n[0].remove(item)
            #if len(n[0]) == 0 : del n[0]
        del n[0]
        print(f'CYCLED THROUGH FIRST SUBLIST, LIST IS NOW {n}')
        if len(n) == 0 : return n
        #templist = [item[len(item) - 1] for item in n]
        #poplist = [item.pop(len(item) - 1) for item in n]
        #for item in templist :
        #    snailist.append(item)
        #templist.clear()
        #poplist.clear()
        #revlist = [n[len(n) - 1]]
        templist = [item[len(item) - 1] for item in n]
        poplist = [item.pop(len(item) - 1) for item in n]
        print(f'CYCLED THROUGH LAST ITEMS, LIST IS NOW {n}')
        for item in templist :
            #print(f'cycling through last in each list, item is {item}')
            snailist.append(item)
        if len(n) == 0 : return n
        templist.clear()
        poplist.clear()
        #for item in n :
        #    print(f'cycling through last in each list, item is {item}')
        #    subitem = item[len(item) - 1]
        #    snailist.append(subitem)
        #    item.remove(subitem)
        for item in reversed(n[len(n) - 1]) :
            #print(f'cycling through last sublist, item is {item}')
            snailist.append(item)
            #n[len(n) - 1].remove(item)
            #if len(n[len(n) - 1]) == 0 : del n[len(n) - 1]
        del n[len(n) - 1]
        if len(n) == 0 : return n
        print(f'CYCLED THROUGH LAST SUBLIST BACKWARDS, LIST IS NOW {n}')
        templist = [item[0] for item in reversed(n)]
        poplist = [item.pop(0) for item in reversed(n)]
        print(f'CYCLED THROUGH FIRST ITEM IN EACH SUBLIST BACKWARDS, LIST IS NOW {n}')
        for item in templist :
            #print(f'cycling through lists backwards, first item is {item}')
            snailist.append(item)
        if len(n) == 0 : return n
        templist.clear()
        poplist.clear()
        return n
    cycle(currentlist)
    while not len(currentlist) == 0 : cycle(currentlist)
    return snailist