#create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
def create_phone_number(n):
    n = [str(x) for x in n]
    if not len(n) == 10 : return ''
    return f"({''.join(n[:3])}) {''.join(n[3:6])}-{''.join(n[6:])}"
print(create_phone_number(list(input())))