def disemvowel(string_):
    return ''.join([i if i.lower() not in ['a','e','i','o','u'] else '' for i in list(string_)])