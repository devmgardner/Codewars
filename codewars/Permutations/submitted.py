from itertools import permutations
def permutations(string):
    return [''.join(x) for x in sorted(list(set([i for i in (sorted(i for i in permutations(string, len(string))))])))]


#OR
import itertools
def permutations(string):
    return [''.join(x) for x in (set([i for i in (itertools.permutations(string, len(string)))]))]