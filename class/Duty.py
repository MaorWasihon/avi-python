
import csv
from datetime import datetime

class DutyData:
    def __init__(self, filename):
        self.filename = filename

    def save(self, dutys):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['employee_id', 'date', 'start_time', 'end_time'])
            for duty in dutys:
                writer.writerow([duty.employee_id, duty.date.strftime('%Y-%m-%d'), duty.start_time, duty.end_time])

    def load(self):
        dutys = []
        with open(self.filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                duty_date = datetime.strptime(row['date'], '%Y-%m-%d').date()
                dutys.append(Duty(int(row['employee_id']), duty_date, int(row['start_time']), int(row['end_time'])))
        return dutys


class Duty:
    def __init__(self, employee_id, date, start_time, end_time):
        self.employee_id = employee_id
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
    
    def duration(self):
        start = datetime.strptime(self.start_time, '%H:%M')
        end = datetime.strptime(self.end_time, '%H:%M')
        return int((end - start).total_seconds() / 60)
    
    def overlap(self, other_duty):
        if self.date != other_duty.date:
            return False
        start1 = datetime.strptime(self.start_time, '%H:%M')
        end1 = datetime.strptime(self.end_time, '%H:%M')
        start2 = datetime.strptime(other_duty.start_time, '%H:%M')
        end2 = datetime.strptime(other_duty.end_time, '%H:%M')
        return (start1 <= end2) and (end1 >= start2)
    
    def conflict(self, duties):
        conflicts = []
        for duty in duties:
            if self.overlap(duty):
                conflicts.append(duty)
        return conflicts

class TestDuty():
    
    def test_duration(self):
        duty = Duty(1, '2023-05-09', '08:00', '10:30')
        duration = duty.duration()
        self.assertEqual(duration, 150)
    
    def test_overlap(self):
        duty1 = Duty(1, '2023-05-09', '08:00', '10:30')
        duty2 = Duty(2, '2023-05-09', '09:30', '12:00')
        duty3 = Duty(3, '2023-05-10', '08:00', '10:30')
        self.assertTrue(duty1.overlap(duty2))
        self.assertTrue(duty2.overlap(duty1))
        self.assertFalse(duty1.overlap(duty3))
        self.assertFalse(duty3.overlap(duty1))
        self.assertFalse(duty2.overlap(duty3))
        self.assertFalse(duty3.overlap(duty2))
    
    def test_conflict(self):
        duty1 = Duty(1, '2023-05-09', '08:00', '10:30')
        duty2 = Duty(2, '2023-05-09', '09:30', '12:00')
        duty3 = Duty(3, '2023-05-10', '08:00', '10:30')
        duty4 = Duty(4, '2023-05-09', '11:00', '13:00')
        duty5 = Duty(5, '2023-05-10', '09:00', '10:00')
        duties = [duty2, duty3, duty4, duty5]
        conflicts = duty1.conflict(duties)
        self.assertEqual(conflicts, [duty2, duty4])

