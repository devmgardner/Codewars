import itertools
fname = 'Permutations-log.txt'
fhand = open(fname, 'w')
fhand.close()
fhand = open(fname, 'r+')
def permutations(string):
    slist = sorted(i for i in itertools.permutations(string, len(string)))
    return [''.join(x) for x in sorted(list(set([i for i in slist])))]