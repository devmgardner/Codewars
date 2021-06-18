def first_non_repeating_letter(string):
    dict = {}
    for char in list(string) : dict[char.lower()] = dict.get(char.lower(), 0) + 1
    for item in list(string) : 
        if dict[item.lower()] == 1 : return item
        else : return ''
first_non_repeating_letter('a')
first_non_repeating_letter('stress')
first_non_repeating_letter('moonmen')
first_non_repeating_letter('')
first_non_repeating_letter('abba')
first_non_repeating_letter('aa')
first_non_repeating_letter('~><#~><')
first_non_repeating_letter('hello world, eh?')
first_non_repeating_letter('sTreSS')
first_non_repeating_letter('Go hang a salami, I\'m a lasgna hog!')