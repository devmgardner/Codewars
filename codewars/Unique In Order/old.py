def unique_in_order(iterable):
    cl = []
    for i,c in enumerate(list(iterable)):
        if list(iterable)[i] == 0 : cl.append(c)
        if len(list(iterable)) == 1 : return list(iterable)
        if not list(iterable)[i] == 0 and not list(iterable)[i-1] == c : cl.append(c)
    print(iterable)
    return cl