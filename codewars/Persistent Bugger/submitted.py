count = 1
def persistence(n):
    numl = list(str(n))
    if len(numl) == 1 : return 0
    total = 1
    for item in numl :
        total *= int(item)
    if len(str(total)) > 1 :
        global count; count += 1
        persistence(total)
    return count
print(persistence(input('')))