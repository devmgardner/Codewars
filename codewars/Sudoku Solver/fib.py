#fname = 'fib-log.txt'
#fhand = open(fname, 'w')
#fhand.close()
#fhand = open(fname, 'r+')
num = [1, 1]
def fib(n, inp):
    #fhand.write(f'input is {inp}\n')
    #fhand.write(f'subnumber 00000000000 is {num[0]}\n')
    #fhand.write(f'subnumber 00000000001 is {num[1]}\n')
    for i in range(int(inp)):
        n.append(n[-1] + n[-2])
        #fhand.write(f"subnumber {'{:011d}'.format(i+2)} is {n[-1]}\n")
    return n[int(inp)]
print(fib(num, input('')))