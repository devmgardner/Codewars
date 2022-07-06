import string

def is_pangram(s):
    print(f'string is {s.lower()}')
    alph = list('abcdefghijklmnopqrstuvwxyz')
    for i in s:
        if i.lower() in alph:
            print(f'letter {i.lower()} still in alph, removing')
            alph.remove(i.lower())
            print(f'alph is now:')
            print(alph)
    if len(alph) == 0:
        return True
    else:
        return False