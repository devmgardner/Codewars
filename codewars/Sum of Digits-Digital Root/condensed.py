def digital_root(n):
    while int(n) >= 10 :
        n = sum(int(i) for i in str(n))
    return int(n)
#digital_root(16)
#digital_root(942)
#digital_root(132189)
#digital_root(493193)
print(digital_root(input('')))