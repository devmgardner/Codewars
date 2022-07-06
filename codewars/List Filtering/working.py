def filter_list(l):
    result = []
    for i in l:
        try:
            j = i + 1
            result.append(i)
        except TypeError:
            continue
    return result