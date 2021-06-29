fname = 'encoder-log.txt'
fhand = open(fname, 'w')
fhand.close()
fhand = open(fname, 'r+')
num = int(input(''))
conv = []
valid = {1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
fhand.write(f'starting value of num is {num}\n')
for n in valid:
    fhand.write(f'n in valid is {n}\n')
    if num >= n:
        fhand.write(f'current num is {num}\n')
        x, y = divmod(num, n)
        num = y
        fhand.write(f'quotient is {x}, remainder is {y}. new num is {num}\n')
        for i in range(x):
            conv.append(valid.get(n))
            fhand.write(f'appending {valid.get(n)}\n')
conv = ''.join(conv)
fhand.write(f'final result is {conv}')
print(conv)



#if num >= 1000:
#    x, y = divmod(num, 1000)
#    for i in range(x):
#        conv.append('M')
#    if y >= 900:
#        a, b = divmod(y, 900)
#        for i in range(a):
#            conv.append('CM')
#    elif y >= 500:
#        a, b = divmod(y, 500)
#        for i in range(a):
#            conv.append('D')
#    elif y >= 400:
#        a, b = divmod(y, 400)
#        for i in range(a):
#            conv.append('CD')
#    elif y >= 100:
#        a, b = divmod(y, 100)
#        for i in range(a):
#            conv.append('C')
#for ind, num in enumerate(list(newl)):
#    for newl[-1] : 
#    conv = []
#    if len(newl) == 4 and ind == 0 :
#        for i in range(int(num)) : conv.append('M')