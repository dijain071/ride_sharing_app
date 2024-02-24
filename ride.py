from uuid import uuid4
from enum import Enum

class RideStatus(Enum):
    ACTIVE = 1
    END = 2

class Ride:
    def __init__(self, shared_by, origin, destination, available_seats, vehicle_number, vehicle_model):
        self.id = uuid4()
        self.shared_by = shared_by
        self.selected_by = []
        self.origin = origin
        self.destination = destination
        self.available_seats = available_seats
        self.status = RideStatus.ACTIVE
        self.vehicle_number = vehicle_number
        self.vehicle_model = vehicle_model

    def get_vehicle_model(self):
        return self.vehicle_model
    
    def get_vehicle_number(self):
        return self.vehicle_number

    def get_id(self):
        return self.id

    def get_shared_by(self):
        return self.shared_by

    def get_selected_by(self):
        return self.selected_by
    
    def get_origin(self):
        return self.origin

    def set_origin(self, origin):
        self.origin = origin

    def get_destination(self):
        return self.destination

    def set_destination(self, destination):
        self.destination = destination

    def get_available_seats(self):
        return self.available_seats

    def get_status(self):
        return self.status
    
    def end_ride(self):
        self.status = RideStatus.END
    
    def add_passenger(self, passenger, seats):
        self.selected_by.append(passenger)
        self.available_seats -= seats

    def __str__(self):
        return f"Ride details: Ride created by {self.shared_by}"

