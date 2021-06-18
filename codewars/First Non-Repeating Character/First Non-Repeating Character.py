def first_non_repeating_letter(string):
    chars = list(string)
    dict = {}
    for char in chars : dict[char.lower()] = dict.get(char.lower(), 0) + 1
    for ind, char in enumerate(chars) :
        if not dict[char.lower()] == 1 : continue
        else : return char; break
    if len(chars) == 0 : return ''
    if not 1 in dict : return ''
print(first_non_repeating_letter(input('')))