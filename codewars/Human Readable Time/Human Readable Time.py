def make_readable(seconds):
    sec = int(seconds)
    if sec > 359999 : sec = 359999
    m, s = divmod(sec, 60)
    h, m = divmod(m, 60)
    return f'{h:02d}:{m:02d}:{s:02d}'
print(make_readable(input('')))