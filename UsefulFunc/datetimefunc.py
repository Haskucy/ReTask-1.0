import datetime

def stringToDatetimeConverter(input):
    text = input.split(",")
    date = text[0]
    time = text[1].split(":")

    if "today" in date:
        date = datetime.date.today().__str__()
    date = date.split("-")

    year = eval(date[0])
    month = eval(date[1])
    dates = eval(date[2])
    hour = eval(time[0])
    minute = eval(time[1])
    second = eval(time[2])

    hasil = datetime.datetime(year, month, dates, hour, minute, second, 0, None)
    return hasil
