import datetime, calendar
from datetime import timedelta, datetime, date, timezone

# appointments = [(datetime(date.today().year, date.today().month, date.today().day, 9, 30, tzinfo=timezone.utc),
#                  datetime(date.today().year, date.today().month, date.today().day, 12, 30, tzinfo=timezone.utc)),
#                 (datetime(date.today().year, date.today().month, date.today().day, 13, 0, tzinfo=timezone.utc),
#                  datetime(date.today().year, date.today().month, date.today().day, 14, 0, tzinfo=timezone.utc)),
#                 (datetime(date.today().year, date.today().month, date.today().day, 16, 30, tzinfo=timezone.utc),
#                  datetime(date.today().year, date.today().month, date.today().day, 17, 0, tzinfo=timezone.utc))
#                 ]
appointments = [(datetime(2023, 10, 25, 9, 30, tzinfo=timezone.utc),
                  datetime(2023, 10, 25, 12, 30, tzinfo=timezone.utc)),
                 (datetime(2023, 10, 25, 13, 0, tzinfo=timezone.utc),
                  datetime(2023, 10, 25, 13, 30, tzinfo=timezone.utc)),
                 ]
def get_slots(appointments, hours=1):
    duration = timedelta(hours=hours)
    current_year = date.today().year
    current_month = date.today().month
    current_day = date.today().day
    hours = (datetime(current_year, current_month, current_day, 8, 0)
             .replace(tzinfo=timezone.utc), datetime(current_year, current_month, current_day, 18, 0)
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
    days = [date(date.today().year, date.today().month, day) for day in range(1, num_days + 1)]
    return days

#
# changed_day_appointments = []
# for one_tuple in appointments:
#     for item in one_tuple:
#         item = item + timedelta(days=1)
#         changed_day_appointments.append(item)
# changed_day_appointments = list(zip(*[changed_day_appointments] * 2))

res = get_slots(appointments)
for i in res:
    print(i)