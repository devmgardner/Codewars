#https://www.codewars.com/kata/55084d3898b323f0aa000546/
def encode_str(strng, shift):
    alph = list('abcdefghijklmnopqrstuvwxyz')
    def caesar_shift(inp,shift,alph):
        strng_list = []
        for i in inp:
            if i.lower() not in alph:
                strng_list.append(i)
            elif i.lower() in alph:
                if i.islower():
                    if alph.index(i) + shift >= len(alph):
                        new_ind = alph.index(i)+shift-len(alph)
                        strng_list.append(alph[new_ind])
                    else:
                        strng_list.append(alph[alph.index(i)+shift])
                elif i.isupper():
                    if alph.index(i.lower()) + shift >= len(alph):
                        new_ind = alph.index(i.lower())+shift-len(alph)
                        strng_list.append(alph[new_ind].upper())
                    else:
                        strng_list.append(alph[alph.index(i.lower())+shift].upper())
        return ''.join(strng_list)
    temp_strng = []
    temp_strng.append(strng[0].lower())
    if alph.index(strng[0].lower()) + shift >= len(alph):
        new_ind = alph.index(strng[0].lower())+shift-len(alph)
        temp_strng.append(alph[new_ind])
    else:
        temp_strng.append(alph[alph.index(strng[0].lower())+shift])
    strng = caesar_shift(strng, shift, alph)
    strng = ''.join(temp_strng)+strng
    length = len(strng)
    if length%4 == 0:
        new_length = int(length/4)
        strng_array = []
        for i in range(4):
            strng_array.append(strng[:new_length])
            strng = strng[new_length:]
        return strng_array
    elif length%5 == 0:
        new_length = int(length/5)
        strng_array = []
        for i in range(5):
            strng_array.append(strng[:new_length])
            strng = strng[new_length:]
        return strng_array
    elif length%4 != 0 and length%5 != 0:
        strng_array = []
        new_length = int(length/5)
        last_length = length%5
        for i in range(4):
            strng_array.append(strng[:new_length])
            strng = strng[new_length:]
        strng_array.append(strng)
        return strng_array



def decode(arr):
    #your code
