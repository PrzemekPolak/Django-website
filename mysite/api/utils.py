def date_set_format(date_time):
    date = date_time.date()
    hour = date_time.hour
    minute = date_time.minute
    second = date_time.second
    return f'{date} {hour}:{minute}:{second}'