#https://www.codewars.com/kata/5390bac347d09b7da40006f6/python
def to_jaden_case(string):
    return ' '.join([word[:1].upper()+word[1:].lower() for word in string.split(' ')])