import string

def is_pangram(s):
    alph = list('abcdefghijklmnopqrstuvwxyz')
    for i in s:
        if i.lower() in alph:
            alph.remove(i.lower())
    if len(alph) == 0:
        return True
    else:
        return False