def format_duration(seconds):
    seconds = int(seconds)
    print(seconds)
    if seconds == 0: return 'now'
    #if seconds > 359999 : seconds = 359999
    #m, s = divmod(seconds, 60)
    #h, m = divmod(m, 60)
    #return f'{h:02d}:{m:02d}:{s:02d}.format(h)'
    years, remainder = divmod(seconds, 31536000)
    days, remainder = divmod(remainder, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, remainder = divmod(remainder, 60)
    final, secs = divmod(remainder, 60)
    if secs == 1: seconds=f'{seconds} second'





    if not years > 0 and not days > 0 and not hours > 0 and not minutes > 0 and secs == 1: return f'{seconds} second'
    elif not years > 0 and not days > 0 and not hours > 0 and not minutes > 0 and secs > 0: return f'{seconds} seconds'
    elif years == 1: years=f'{years} year, '
    elif years > 0: years=f'{years} years, '
    #
    if days == 1: days=f'{days} day, '
    elif days > 0: days=f'{days} days, '
    #
    if hours == 1 and minutes > 0 or hours == 1 and secs > 0: hours=f'{hours} hour, '
    elif hours == 1 and not minutes > 0 and not secs > 0: hours=f'{hours} hour'
    elif hours > 0 and minutes > 0 or hours > 0 and secs > 0:hours=f'{hours} hours, '
    elif hours > 0 and not minutes > 0 and not secs > 0:hours=f'{hours} hours'
    #
    if minutes == 1 and secs > 0:minutes=f'{minutes} minute and {secs} seconds'
    elif minutes == 1 and secs == 1:minutes=f'{minutes} minute and {secs} second'
    elif minutes == 1 and not secs > 0:minutes=f'and {minutes} minute'
    elif minutes > 0 and secs == 1: minutes=f'{minutes} minutes and {secs} second'
    elif minutes > 0 and secs > 0:minutes=f'{minutes} minutes and {secs} seconds'
    elif minutes > 0 and not secs > 0:minutes=f'and {minutes} minutes'
    elif not minutes > 0 and secs == 1:minutes=f'and {secs} second'
    elif not minutes > 0 and secs > 0:minutes=f'and {secs} seconds'
    result = [years, days, hours, minutes]
    return ''.join([i for i in result if not isinstance(i, int)])
    #if seconds >= 31536000:
    #    years, remainder = divmod(seconds, 31536000)
    #    if remainder >= 86400:
    #        days, remainder = divmod(remainder, 86400)
    #    if remainder >= 3600:
    #        hours, remainder = divmod(remainder, 3600)
    #    if remainder >= 60:
    #        minutes, remainder = divmod(remainder, 60)
    #    if remainder >= 0:
    #        final, secs = divmod(remainder, 60)
    #print(str(seconds).format(f'{years} years, {days} days, {hours} hours, {minutes} minutes and {secs} seconds.'))
    #return str(years) + str(days) + str(hours) + str(minutes) + str(secs)
print(format_duration(input()))