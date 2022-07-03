#https://www.codewars.com/kata/5264d2b162488dc400000001/
def spin_words(sentence):
    sentence = ''.join(sentence)
    result = []
    for word in sentence.split(' '):
        if len(word) < 5:
            result.append(word)
        elif len(word) >= 5:
            result.append(''.join(reversed(list(word))))
    return ' '.join(result)