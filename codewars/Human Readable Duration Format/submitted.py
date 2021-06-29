def format_duration(seconds):
    seconds = int(seconds)
    if seconds == 0: return 'now'
    years, remainder = divmod(seconds, 31536000)
    days, remainder = divmod(remainder, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, remainder = divmod(remainder, 60)
    final, secs = divmod(remainder, 60)
    if secs > 0: ssecs=f'{secs} second'
    else:ssecs=None
    if minutes > 0: sminutes=f'{minutes} minute'
    else:sminutes=None
    if hours > 0: shours=f'{hours} hour'
    else:shours=None
    if days > 0: sdays=f'{days} day'
    else:sdays=None
    if years > 0: syears=f'{years} year'
    else:syears=None
    comp = {ssecs:secs,sminutes:minutes,shours:hours,sdays:days,syears:years}
    list = [syears, sdays, shours, sminutes, ssecs]; result = []
    for i in list:
        if comp.get(i) > 1: result.append(str(i) + 's')
        elif comp.get(i) == 1: result.append(str(i))
        elif comp.get(i) is None: continue
    if len(result) > 1:result[-2]+=' and '
    if len(result) == 5:
        for i in range(3):result[i]+= ', '
    if len(result) == 4:
        for i in range(2):result[i]+= ', '
    elif len(result) == 3:
        result[0] += ', '
    return ''.join(result)