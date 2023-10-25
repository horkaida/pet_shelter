from datetime import datetime, timezone

import unittest
from function_schedule import get_slots
class TestSchedule(unittest.TestCase):
    appointments = [(datetime(2023, 10, 24, 9, 30, tzinfo=timezone.utc),
                     datetime(2023, 10, 24, 12, 30, tzinfo=timezone.utc)),
                    (datetime(2023, 10, 24, 13, 0, tzinfo=timezone.utc),
                     datetime(2023, 10, 24, 14, 0, tzinfo=timezone.utc))]

    def test_schedule_available_slots(self):
        available_slots = get_slots(appointments=self.appointments, chosen_day=24, chosen_month=10, chosen_year=2023, hours=1)
        expected_res = [datetime(2023, 10, 24, 8, 0, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 8, 15, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 14, 15, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 14, 30, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 14, 45, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 15, 0, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 15, 15, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 15, 30, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 15, 45, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 16, 0, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 16, 15, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 16, 30, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 16, 45, tzinfo=timezone.utc)]
        self.assertEqual(expected_res, available_slots)

    def test_schedule_duration_2hour(self):
        available_slots = get_slots(appointments=self.appointments, chosen_day=24, chosen_month=10, chosen_year=2023, hours=2)
        expected_res = [datetime(2023, 10, 24, 14, 15, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 14, 30, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 14, 45, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 15, 0, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 15, 15, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 15, 30, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 15, 45, tzinfo=timezone.utc)]
        self.assertEqual(expected_res, available_slots)

    def test_schedule_duration_3hour(self):
        available_slots = get_slots(appointments=self.appointments, chosen_day=24, chosen_month=10, chosen_year=2023, hours=3)
        expected_res = [
                        datetime(2023, 10, 24, 14, 15, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 14, 30, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 14, 45, tzinfo=timezone.utc)]
        self.assertEqual(expected_res, available_slots)

    def test_schedule_change_day(self):
        #the function only works with filtered appointments by the selected date;
        #in case appointments are not filtered in the view, function returns an empty list
        available_slots = get_slots(appointments=self.appointments, chosen_day=25, chosen_month=10, chosen_year=2023, hours=1)
        expected_res = []
        self.assertEqual(expected_res, available_slots)

    def test_schedule_change_month(self):
        available_slots = get_slots(appointments=self.appointments, chosen_day=24, chosen_month=9, chosen_year=2023, hours=1)
        expected_res = []
        self.assertEqual(expected_res, available_slots)

    def test_schedule_change_year(self):
        available_slots = get_slots(appointments=self.appointments, chosen_day=24, chosen_month=10, chosen_year=2020, hours=1)
        expected_res = []
        self.assertEqual(expected_res, available_slots)


    def test_no_available_slots(self):
        appointments = [(datetime(2023, 10, 24, 8, 00, tzinfo=timezone.utc),
                         datetime(2023, 10, 24, 9, 15, tzinfo=timezone.utc)),
                        (datetime(2023, 10, 24, 9, 30, tzinfo=timezone.utc),
                         datetime(2023, 10, 24, 12, 30, tzinfo=timezone.utc)),
                        (datetime(2023, 10, 24, 12, 45, tzinfo=timezone.utc),
                         datetime(2023, 10, 24, 15, 45, tzinfo=timezone.utc)),
                        (datetime(2023, 10, 24, 16, 00, tzinfo=timezone.utc),
                         datetime(2023, 10, 24, 17, 45, tzinfo=timezone.utc))]

        expected_res = []
        available_slots = get_slots(appointments=appointments, chosen_year=2023, chosen_day=24, chosen_month=10, hours=1)
        self.assertEqual(expected_res, available_slots)


    def test_all_slots_available(self):
        appointments = []
        available_slots = get_slots(appointments=appointments, chosen_year=2023, chosen_day=24, chosen_month=10, hours=1)
        expected_res = [datetime(2023, 10, 24, 8, 0, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 8, 15, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 8, 30, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 8, 45, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 9, 0, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 9, 15, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 9, 30, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 9, 45, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 10, 0, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 10, 15, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 10, 30, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 10, 45, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 11, 0, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 11, 15, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 11, 30, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 11, 45, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 12, 0, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 12, 15, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 12, 30, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 12, 45, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 13, 0, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 13, 15, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 13, 30, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 13, 45, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 14, 0, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 14, 15, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 14, 30, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 14, 45, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 15, 0, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 15, 15, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 15, 30, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 15, 45, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 16, 0, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 16, 15, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 16, 30, tzinfo=timezone.utc),
                        datetime(2023, 10, 24, 16, 45, tzinfo=timezone.utc)]
        self.assertEqual(expected_res, available_slots)





