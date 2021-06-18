def unique_in_order(iterable):
    cl = []
    for i,c in enumerate(list(iterable)):
        while i < len(list(iterable)) - 1 :
            if not list(iterable)[i-1] == c : cl.append(c)
    return cl
print(unique_in_order(input('')))