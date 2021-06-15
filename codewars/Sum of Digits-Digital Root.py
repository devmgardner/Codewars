n = input('')
def digital_root(n):
    while int(n) >= 10 :
    #print(f'at start of func, n is {n}')
    #ints = list()
    #for num in str(n).split() : ints.extend(num)
    #print(f'after n was split, the list is {ints}')
    #ints = [int(i) for i in ints]
        n = sum(int(i) for i in str(n))
    return int(n)
    #print(f'sum of list is {n}')
#        if len(str(n)) > 1 :
#            digital_root(n)
#        else : return n
#
#digital_root(16)
#digital_root(942)
#digital_root(132189)
#digital_root(493193)
print(digital_root(n))