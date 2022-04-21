#  вывести время

duration = int(input('Введите целое число: '))

if duration < 60:
    print(duration, 'сек')

elif 60 <= duration < (60 * 60):
    minutes = duration // 60
    seconds = duration % 60
    print(minutes, 'мин', seconds, 'сек')

elif 3600 <= duration < (3600 * 24):
    hours = duration // 3600
    minutes = (duration % 3600) // 60
    seconds = duration % 60
    print(hours, 'час', minutes, 'мин', seconds, 'сек')

elif 86400 <= duration:
    days = duration // 86400
    hours = (duration % 86400) // 3600
    minutes = (duration % 3600) // 60
    seconds = duration % 60
    print(days, 'дн', hours, 'час', minutes, 'мин', seconds, 'сек')

"""
elif 604800 <= duration < 2629743:
    weeks = duration // 2629743
    days = (duration % 604800) // 86400
    hours = (duration % 86400) // 3600
    minutes = (duration % 3600) // 60
    seconds = duration % 60
    print(weeks, 'нед', days, 'дн', hours, 'час', minutes, 'мин', seconds, 'сек')

elif 2629743 <= duration < 31556926:
    month = duration // 2629743
    weeks = (duration % 2629743) // 604800
    days = (duration % 604800) // 86400
    hours = (duration % 86400) // 3600
    minutes = (duration % 3600) // 60
    seconds = duration % 60
    print(month, 'мес', weeks, 'нед', days, 'дн', hours, 'час', minutes, 'мин', seconds, 'сек')
else:
    years = duration // 31556926
    month = (duration % 31556926) // 2629743
    weeks = (duration % 2629743) // 604800
    days = (duration % 604800) // 86400
    hours = (duration % 86400) // 3600
    minutes = (duration % 3600) // 60
    seconds = duration % 60
    print(years, 'г', month, 'мес', weeks, 'нед', days, 'дн', hours, 'час', minutes, 'мин', seconds, 'сек')

"""
