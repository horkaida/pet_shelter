from datetime import datetime, timezone, timedelta, date


import unittest
from function_schedule import get_slots
class TestSchedule(unittest.TestCase):
    appointments = [(datetime(date.today().year, date.today().month, date.today().day, 9, 30, tzinfo=timezone.utc),
                     datetime(date.today().year, date.today().month, date.today().day, 12, 30, tzinfo=timezone.utc)),
                    (datetime(date.today().year, date.today().month, date.today().day, 13, 0, tzinfo=timezone.utc),
                     datetime(date.today().year, date.today().month, date.today().day, 14, 0, tzinfo=timezone.utc)),
                    (datetime(date.today().year, date.today().month, date.today().day, 16, 30, tzinfo=timezone.utc),
                     datetime(date.today().year, date.today().month, date.today().day, 17, 0, tzinfo=timezone.utc))
                    ]
    timeslot = 1
    def test_schedule_available_slots(self):
        available_slots = get_slots(appointments=self.appointments, hours=self.timeslot)
        expected_res = [datetime(date.today().year, date.today().month, date.today().day, 8, 0, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, date.today().day, 8, 15, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, date.today().day, 14, 15, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, date.today().day, 14, 30, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, date.today().day, 14, 45, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, date.today().day, 15, 0, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, date.today().day, 15, 15, tzinfo=timezone.utc)]
        self.assertEquals(available_slots, expected_res)

    def test_schedule_duration_2hour(self):
        available_slots = get_slots(appointments=self.appointments, hours=2)
        expected_res = [(datetime(date.today().year, date.today().month, date.today().day, 14, 15, tzinfo=timezone.utc))]
        self.assertEquals(available_slots, expected_res)

    def test_schedule_duration_3hour(self):
        available_slots = get_slots(appointments=self.appointments, hours=3)
        expected_res = []
        self.assertEquals(available_slots, expected_res)

    def test_schedule_change_day(self):
        changed_day_appointments = []
        for one_tuple in self.appointments:
            for item in one_tuple:
                item = item + timedelta(days=1)
                changed_day_appointments.append(item)
        changed_day_appointments = list(zip(*[changed_day_appointments] * 2))
        available_slots = get_slots(appointments=changed_day_appointments, hours=self.timeslot)
        expected_res = [datetime(date.today().year, date.today().month, 24, 8, 0, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 8, 15, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 8, 30, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 8, 45, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 9, 0, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 9, 15, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 9, 30, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 9, 45, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, date.today().month, 0, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, date.today().month, 15, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, date.today().month, 30, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, date.today().month, 45, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 11, 0, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 11, 15, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 11, 30, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 11, 45, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 12, 0, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 12, 15, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 12, 30, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 12, 45, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 13, 0, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 13, 15, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 13, 30, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 13, 45, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 14, 0, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 14, 15, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 14, 30, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 14, 45, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 15, 0, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 15, 15, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 15, 30, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 15, 45, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 16, 0, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 16, 15, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 16, 30, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 16, 45, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 18, 0, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 18, 15, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 18, 30, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 18, 45, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 19, 0, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 19, 15, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 19, 30, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 19, 45, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 20, 0, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 20, 15, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 20, 30, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 20, 45, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 21, 0, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 21, 15, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 21, 30, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 21, 45, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 22, 0, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 22, 15, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 22, 30, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 22, 45, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 23, 0, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 23, 15, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 23, 30, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, 24, 23, 45, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, date.today().day, 0, 0, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, date.today().day, 0, 15, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, date.today().day, 0, 30, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, date.today().day, 0, 45, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, date.today().day, 1, 0, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, date.today().day, 1, 15, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, date.today().day, 1, 30, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, date.today().day, 1, 45, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, date.today().day, 2, 0, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, date.today().day, 2, 15, tzinfo=timezone.utc),                        datetime(date.today().year, date.today().month, date.today().day, 2, 30, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, date.today().day, 2, 45, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, date.today().day, 3, 0, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, date.today().day, 3, 15, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, date.today().day, 3, 30, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, date.today().day, 3, 45, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, date.today().day, 4, 0, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, date.today().day, 4, 15, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, date.today().day, 4, 30, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, date.today().day, 4, 45, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, date.today().day, 5, 0, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, date.today().day, 5, 15, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, date.today().day, 5, 30, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, date.today().day, 5, 45, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, date.today().day, 6, 0, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, date.today().day, 6, 15, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, date.today().day, 6, 30, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, date.today().day, 6, 45, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, date.today().day, 7, 0, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, date.today().day, 7, 15, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, date.today().day, 7, 30, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, date.today().day, 7, 45, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, date.today().day, 8, 0, tzinfo=timezone.utc),
                        datetime(date.today().year, date.today().month, date.today().day, 8, 15, tzinfo=timezone.utc)]
        self.assertEquals(available_slots, expected_res)


