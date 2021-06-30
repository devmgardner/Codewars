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
    return [''.join(x) for x in sorted(list(set([i for i in slist])))]
    #test = [list(string) for i in range(len(string))]
    #return slist
    #print(slist[0])