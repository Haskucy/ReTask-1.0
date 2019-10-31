import datetime

def stringToDatetimeConverter(input):
    text = input.split(",")
    date = text[0]
    time = text[1].split(":")

    if "today" in date:
        date = datetime.date.today().__str__()
    date = date.split("-")

    year = int(str((date[0])))
    month = int(str((date[1])))
    dates = int(str((date[2])))
    hour = int(str((time[0])))
    minute = int(str((time[1])))
    second = int(str((time[2])))

    hasil = datetime.datetime(year, month, dates, hour, minute, second, 0, None)
    return hasil

def DatetimeCount(input):
    inputtext = input.__str__()
    text = text = inputtext.split(" ")
    date = text[0].split("-")
    time = text[1].split(":")

    year = str(date[0])
    month = str(date[1])
    dates = str(date[2])
    hour = str(time[0])
    minute = str(time[1])

    se = str(time[2])
    set = se.split(".")
    second = str(set[0])


    hasil = int(year+month+dates+hour+minute+second)

    return hasil
