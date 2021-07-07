import json, re, string, itertools, os, sys
fname = 'sum-the-nums-starting-log.txt'
fhand = open(fname, 'w')
fhand.close()
fhand = open(fname, 'r+')
#
def sumnum(n):
    return sum([i+1 for i in range(n)])
#
def sumnum2(n):
    return sum([sumnum(i+1) for i in range(n)])
def sum_of_sums(n):
    return sumnum(sumnum2(n))
#
inp = int(input())
print(f'sumnum is {sumnum(inp)}')
print(f'sumnum2 is {sumnum2(inp)}')
print(f'sum_of_sums is {sum_of_sums(inp)}')