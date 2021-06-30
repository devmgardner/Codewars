import itertools
fname = 'Permutations-log.txt'
fhand = open(fname, 'w')
fhand.close()
fhand = open(fname, 'r+')
def permutations(string):
    #your code here
    #slist = list(string)
    #slist = sorted([i for i in list(itertools.product(x, y))] for x in list(string) for y in list(string))
    slist = sorted([i for i in list(itertools.product(*[list(string) for i in range(len(string))]))])
    slist = [''.join(x) for x in slist]
    test = [zip(''.join(sorted(list(item))), ''.join(sorted(list(string)))) for item in slist]
    test = [list(item) for item in test]
    results = []
    for item in test:
        res = []
        for tup in item:
            print(tup)
            if tup[0] == tup[1]: res.append(True)
            else: res.append(False)
        if all(i for i in res) == True: results.append(item)
        else: continue
    final = []
    for item in results:
        word = []
        print(item)
        #for i in range(len(item)):
        #    word.append(item[i][0])
        #final.append(''.join(word))
    #results = [True if tup[0] == tup[1] else False for tup in item for item in test]
    return None
    ###        if not tup[0] == tup[1]: test.remove(item)
    #return test







    #slist = [item for item in slist for char in item if list(string).count(char) == item.count(char)]
    ###newlist = []
    ###for item in slist:
    ###    for char in item:
    ###        if item.count(char) == list(string).count(char): newlist.append(item)
    #for item in slist:
    #    for char in item:
    #        if list(string.count(char)) != item.count(char): continue

    #return [''.join(x) for x in sorted(list(set([i for i in newlist])))]
    #test = [list(string) for i in range(len(string))]
    ####return slist
    #print(slist[0])
print(permutations(input('')))