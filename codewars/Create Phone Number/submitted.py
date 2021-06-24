def create_phone_number(n):
    n = [str(x) for x in n]
    if not len(n) == 10 : return ''
    return f"({''.join(n[:3])}) {''.join(n[3:6])}-{''.join(n[6:])}"