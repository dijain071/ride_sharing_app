from uuid import UUID
from edge_cases import (AlreadyRideExists)

class RideManager:
    def __init__(self):
        self.activeRides = {}

    def get_active_rides(self):
        return self.activeRides

    def add_offer_ride(self, ride, user_name):
        for r in self.activeRides.values():
            if r.vehicle_number == ride.vehicle_number:
                raise AlreadyRideExists()
        self.activeRides[ride.id] = ride

    def end_ride(self, vehicle_number):
        for ride in self.activeRides.values():
            if ride.vehicle_number == vehicle_number:
                return ride
        return None
