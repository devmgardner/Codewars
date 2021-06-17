def first_non_repeating_letter(string):
    dict={}
    for char in list(string) : dict[char] = dict.get(char, 0) + 1
    for item in list(string) : 
        if dict[item] == 1 : return item