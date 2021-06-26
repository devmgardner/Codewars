def snail(snail_map):
    snailist=[]
    if len(snail_map)==1:
        oneresult=[]
        for item in snail_map[0]:oneresult.append(item)
        return oneresult
    if len(snail_map)==2:
        tworesult=[]
        for item in snail_map[0]:tworesult.append(item)
        for item in reversed(snail_map[1]):tworesult.append(item)
        return tworesult
    if len(snail_map)==0:return ''
    currentlist=snail_map
    def cycle(n):
        for item in n[0]:snailist.append(item)
        del n[0]
        if len(n)==0:return n
        templist=[item[len(item)-1] for item in n]
        poplist=[item.pop(len(item)-1) for item in n]
        for item in templist:snailist.append(item)
        if len(n)==0:return n
        templist.clear();poplist.clear()
        for item in reversed(n[len(n)-1]):snailist.append(item)
        del n[len(n)-1]
        if len(n)==0:return n
        templist=[item[0] for item in reversed(n)]
        poplist=[item.pop(0) for item in reversed(n)]
        for item in templist:snailist.append(item)
        if len(n)==0:return n
        templist.clear();poplist.clear()
        return n
    cycle(currentlist)
    while not len(currentlist)==0:cycle(currentlist)
    return snailist