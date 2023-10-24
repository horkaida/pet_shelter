import datetime, calendar
from datetime import timedelta, datetime, date, timezone

def get_slots(appointments, chosen_day, chosen_month, chosen_year, hours=1):
    duration = timedelta(hours=hours)
    hours = (datetime(chosen_year, chosen_month, chosen_day, 8, 0)
             .replace(tzinfo=timezone.utc), datetime(chosen_year, chosen_month, chosen_day, 18, 0)
             .replace(tzinfo=timezone.utc))
    available_slots = []
    new_app = []
    for i in range(len(appointments)):
        new_app.append((appointments[i][0], appointments[i][1] + timedelta(minutes=15)))
    slots = sorted([(hours[0], hours[0])] + new_app + [(hours[1], hours[1])])
    for freetime_start, freetime_end in ((slots[i][1], slots[i + 1][0]) for i in range(len(slots) - 1)):
        assert freetime_start <= freetime_end
        while freetime_start + duration <= freetime_end - timedelta(minutes=15):
            available_slots.append(freetime_start)
            freetime_start += timedelta(minutes=15)
    return available_slots

def get_calendar():
    num_days = calendar.monthrange(date.today().year, date.today().month)[1]
    days = [date(date.today().year, date.today().month, day) for day in range(1, num_days+1)]
    return days
