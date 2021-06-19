import string
def pig_it(text):
    sentlist = []
    if len(text) == 0 or len(text) == 1 : return ''
    print(f'split text is {text.split()}')
    for word in text.split() :
        def move(w) :
            wlist.append(wlist[0]) ; wlist.pop(0) ; wlist.append('ay')
        print(f'word is {word}')
        wlist = list(word)
        print(f'  wlist is {wlist}')
        if len(word) == 1 and not wlist[0] in string.punctuation :
            print(wlist[0])
            print(f'   len is 1, not in punctuation')
            wlist.append('ay')
            break
        elif len(word) == 1 and wlist[0] in string.punctuation :
            print(wlist[0])
            print(f'    len is 1, and is punctuation')
        elif not len(word) == 1 and wlist[len(wlist) - 1] in string.punctuation :
            last = wlist[len(wlist) - 1]
            print(f'  wlist is full word with punctuation at end')
            print(f'last character is {last}')
            p = wlist[len(wlist) - 1]
            print(f'     p is {p}')
            wlist.pop(len(wlist) - 1)
            move(wlist)
            print(f'  wlist after function is {wlist}')
            wlist.append(p)
        elif not len(word) == 1 and not wlist[len(wlist) - 1] in string.punctuation :
            move(wlist)
        wlist = ''.join(wlist)
        print(f'    --wlist after join is {wlist}')
        sentlist.append(wlist)
    sentlist = ' '.join(sentlist)
    return(sentlist)
print(pig_it(input('')))