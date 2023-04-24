from .models import LastUpdate
import datetime

def update(type):
    hr = datetime.datetime.now().hour
    if hr >= 6 and hr < 18:
        t = 6
    elif hr >= 18 or hr < 6:
        t = 18
    LastUpdate.objects.filter(type = type).delete()
    LastUpdate.objects.create(hour = str(t),
                              day = str(datetime.datetime.now().day),
                              month = str(datetime.datetime.now().month),
                              year = str(datetime.datetime.now().year),
                              type = type)
    return

def needupdate(type):

    currentHour = datetime.datetime.now().hour
    currentDay = datetime.datetime.now().day
    currentMonth = datetime.datetime.now().month
    currentYear = datetime.datetime.now().year

    date = LastUpdate.objects.filter(type = type).first()
    upd = False
    if int(date.year) < currentYear:
        upd = True
    elif int(date.month) < currentMonth:
        upd = True
    elif int(date.day) < currentDay:
        upd = True
    elif int(date.hour) == 18 and currentHour >= 6 and currentHour < 18:
        upd = True
    elif int(date.hour) == 6 and (currentHour >= 18 or currentHour < 6):
        upd = True

    return upd
    
    
