import string
def pig_it(text):
    sentlist = []
    if len(text) == 0 : return ''
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
            print(f'  after ay is {wlist}')
        elif len(word) == 1 and wlist[0] in string.punctuation : wlist.append('')
        elif not len(word) == 1 and wlist[len(wlist) - 1] in string.punctuation :
            p = wlist[len(wlist) - 1]
            wlist.pop(len(wlist) - 1)
            move(wlist)
            wlist.append(p)
        elif not len(word) == 1 and not wlist[len(wlist) - 1] in string.punctuation :
            move(wlist)
        if not len(wlist) <= 1 :
            wlist = ''.join(wlist)
        elif len(wlist) <= 1 : wlist = str(wlist[0])
        sentlist.append(wlist)
    sentlist = ' '.join(sentlist)
    return(sentlist)