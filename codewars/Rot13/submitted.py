alph = 'abcdefghijklmnopqrstuvwxyz'
ualph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def rot13(message):
    letrs = []
    for char in message :
        if not char in alph and not char in ualph : letrs.append(char)
        elif char.isupper() :
            ind = ualph.index(char)
            ind += 13
            if ind > 25 : ind -= 26
            letrs.append(ualph[ind])
        elif char.islower() :
            ind = alph.index(char)
            ind += 13
            if ind > 25 : ind -= 26
            letrs.append(alph[ind])
    letrs = str(''.join(letrs))
    return letrs