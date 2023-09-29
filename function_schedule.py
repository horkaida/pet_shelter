import datetime
from datetime import timedelta

appointments = [(datetime.datetime(2017, 9, 7, 9, 30),
                 datetime.datetime(2017, 9, 7, 12, 30)),
                (datetime.datetime(2017, 9, 7, 13, 0),
                 datetime.datetime(2017, 9, 7, 14, 0)),
                ]


def get_slots(appointments, duration=timedelta(hours=1)):
    hours = (datetime.datetime(2017, 9, 7, 8, 0), datetime.datetime(2017, 9, 7, 18, 0))
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
