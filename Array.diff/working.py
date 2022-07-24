#https://www.codewars.com/kata/523f5d21c841566fde000009/python
def array_diff(a, b):
    for i in b:
        while i in a:
            a.remove(i)
    return a