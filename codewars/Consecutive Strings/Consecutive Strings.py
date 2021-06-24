fname = 'consecutivestringslog.txt'
fhand = open(fname, 'w')
fhand.close()
fhand = open(fname, 'r+')
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
    fhand.write(f'strarrstr after join with space delimiter is {strarrstr}\n')
    fhand.write(f'words list is {words}\n')
    #fhand.write(f'{}')
    #fhand.write(f'{}')
    #fhand.write(f'{}')
    #fhand.write(f'{}')
    while (count + int(k) - 2) < (len(words)) : 
        iteratorlist = []
        total = 0
        setlist = []
        fhand.write(f'list of iterators is: ')
        for i in range(int(k)) :
            iteratorlist.append(i + count - 1)
            fhand.write(f'{i}, ')
        fhand.write(f'\n')
        for iterator in iteratorlist :
            total += len(words[iterator])
            setlist.append(words[iterator])
        fhand.write(f'{setlist} is list of words, {total} is the total count of characters\n')
        tuplelist.append( (count, setlist, total) )
        count += 1
    tuplelist.sort(key=lambda tup: (tup[2],tup[0]), reverse=True)
    fhand.write(f'{tuplelist} is final list containing an index, the list of words starting at index-1, and the total number of characters in that list, sorted first by count and then by index\n')
    maxcount = tuplelist[0][2]
    finaltuplist = []
    for tup in tuplelist :
        if tup[2] == maxcount :
            finaltuplist.append(tup)
    finaltuplist.sort(key=lambda tup: tup[0])
    fhand.write(f'{finaltuplist} is final list of strings with the maximum amount of characters, sorted by the order in which they appear in the original input')
    return ''.join(finaltuplist[0][1])
print(longest_consec(list(input()), input('')))