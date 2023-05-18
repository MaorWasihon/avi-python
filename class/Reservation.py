import csv
import datetime

class ReservationData:
    def __init__(self, filename):
        self.filename = filename

    def save(self, reservations):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['reservation_id', 'customer_id', 'table_id', 'reservation_time'])
            for reservation in reservations:
                writer.writerow([reservation.reservation_id, reservation.customer_id, reservation.table_id, reservation.reservation_time])

    def load(self):
        reservations = []
        with open(self.filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                reservation = Reservation(int(row['reservation_id']), int(row['customer_id']), int(row['table_id']), datetime.datetime.fromisoformat(row['reservation_time']))
                reservations.append(reservation)
        return reservations

class Reservation:
    def __init__(self, reservation_id, customer_id, table_id, reservation_time):
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.table_id = table_id
        self.reservation_time = reservation_time
        self.status = None

    def reserve_table(self, reservation_id, customer_id, reservation_time):
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.reservation_time = reservation_time
        self.status = 'reserved'

    def create_reservation(self, reservation_id, customer_id, table_id, reservation_time):
        reservation = Reservation(reservation_id, customer_id, table_id, reservation_time)
        reservation.status = 'reserved'
        return reservation

    def update_reservation(self, reservation_id, table_id, reservation_time):
        if self.reservation_id == reservation_id:
            self.table_id = table_id
            self.reservation_time = reservation_time
            return True
        else:
            return False

    def delete_reservation(self, reservation_id):
        if self.reservation_id == reservation_id:
            del self
            return True
        else:
            return False

def test_reservation():
    # create a reservation object
    reservation = Reservation(1, 1, 1, datetime.datetime(2023, 5, 20, 18, 0))

    # check that the reservation was created with the correct attributes
    assert reservation.reservation_id == 1
    assert reservation.customer_id == 1
    assert reservation.table_id == 1
    assert reservation.reservation_time == datetime.datetime(2023, 5, 20, 18, 0)

    # test the reserve_table method
    reservation.reserve_table(2, 456, datetime.datetime(2023, 5, 20, 18, 0))
    assert reservation.reservation_id == 2
    assert reservation.customer_id == 456
    assert reservation.reservation_time == datetime.datetime(2023, 5, 20, 18, 0)
    assert reservation.status == 'reserved'

