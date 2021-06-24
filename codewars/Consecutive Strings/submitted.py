def longest_consec(strarr, k):
    # your code
    strarrstr = []
    for item in strarr :
        strarrstr.append(item)
    if int(k) < 1 : return ''
    if len(strarr) < 1 : return ''
    if len(strarr) == 1 : return strarr[0]
    if int(k) > (len(strarr) - 1) : return ''
    strarrstr = ' '.join(strarrstr)
    words = strarrstr.split()
    count = 1
    tuplelist = []
    while (count + int(k) - 2) < (len(words)) : 
        iteratorlist = []
        total = 0
        setlist = []
        for i in range(int(k)) :
            iteratorlist.append(i + count - 1)
        for iterator in iteratorlist :
            total += len(words[iterator])
            setlist.append(words[iterator])
        tuplelist.append( (count, setlist, total) )
        count += 1
    tuplelist.sort(key=lambda tup: (tup[2],tup[0]), reverse=True)
    maxcount = tuplelist[0][2]
    finaltuplist = []
    for tup in tuplelist :
        if tup[2] == maxcount :
            finaltuplist.append(tup)
    finaltuplist.sort(key=lambda tup: tup[0])
    return ''.join(finaltuplist[0][1])