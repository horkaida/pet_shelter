import datetime, calendar
from datetime import timedelta, datetime, date, timezone

appointments = [(datetime(2023, 10, 19, 9, 30),
                 datetime(2023, 10, 19, 12, 30)),
                (datetime(2023, 10, 19, 13, 0),
                 datetime(2023, 10, 19, 13, 30)),
                ]

# def chunkwise(t, size=2):
#     it = iter(t)
#     return list(zip(*[it]*size))

def get_slots(appointments, hours=1):
    # aware_tzinfo_appointments = []
    # for one_tuple in appointments:
    #     for split_tuple in one_tuple:
    #         split_tuple = split_tuple.replace(tzinfo=timezone.utc)
    #         aware_tzinfo_appointments.append(split_tuple) #Add tzinfo to dataime
    # appointments = chunkwise(aware_tzinfo_appointments) #Modify dataime
    # print(f'MODIFIED {appointments}')
    duration = timedelta(hours=hours)
    current_year = date.today().year
    current_month = date.today().month
    current_day = date.today().day
    hours = (datetime(current_year, current_month, current_day, 8, 0).replace(tzinfo=timezone.utc), datetime(current_year, current_month, current_day, 18, 0).replace(tzinfo=timezone.utc))
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
    current_year = date.today().year
    current_month = date.today().month
    num_days = calendar.monthrange(current_year, current_month)[1]
    days = [date(current_year, current_month, day) for day in range(1, num_days+1)]
    return days

# rezult = get_slots(appointments)
# print(rezult)

#
# rezult = chunkwise(aware_tzinfo_appointments)
# print(rezult)