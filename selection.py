from enum import Enum
from edge_cases import (NoRideFound)


class SelectionStrategyType(Enum):
    PREFERRED = 1
    MOST_VACANT = 2

class SelectionStrategy:
    def find_rides(self, origin, destination, seats, ride_manager, vehicle_number):
        pass

class PreferredVehicleStrategy(SelectionStrategy):
    def find_preferred_rides(self, origin, destination, seats, ride_manager, vehicle):
        active_rides = ride_manager.get_active_rides()
        potential_ride = None
        
        for ride in active_rides.values():
            if (ride.get_destination() == destination and
                ride.get_origin() == origin and
                ride.get_available_seats() >= seats and
                ride.get_vehicle_model() == vehicle):
                potential_ride = ride
                break
                
        if potential_ride is None:
            raise NoRideFound()
        
        return potential_ride

class MostVacantStrategy(SelectionStrategy):
    def find_vacant_rides(self, origin, destination, seats, ride_manager, vehicle):
        active_rides = ride_manager.get_active_rides()
        potential_ride = None
        max_availability = 0
        
        for ride in active_rides.values():
            if (ride.get_destination() == destination and
                ride.get_origin() == origin and
                ride.get_available_seats() >= seats):
                if ride.get_available_seats() > max_availability:
                    max_availability = ride.get_available_seats()
                    potential_ride = ride
                    
        if potential_ride is None:
            raise NoRideFound()
        
        return potential_ride
