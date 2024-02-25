from DataStore.rideManage import RideManager
from DataStore.userDetails import UserManager
from vehicle import Vehicle
from user import User
from ride import Ride
from edgeCases import (InvalidVehicle, NoRideFound)
from selection import (SelectionStrategyType, PreferredVehicleStrategy, MostVacantStrategy)


class Application:
    def __init__(self):
        self.rideManager = RideManager()
        self.userManager = UserManager()

    def add_user(self, name, gender, age):
        try:
            user = User(name, gender, age)
            self.userManager.add_user(user)
        except Exception as e:
            print(e)

    def add_vehicle(self, user_name, model, vehicle_number):
        try:
            vehicle = Vehicle(user_name, model, vehicle_number)
            user = self.userManager.get_user(user_name)
            user.add_vehicle(vehicle)
        except Exception as e:
            print(e)

    def offer_ride(self, user_name, origin, available_seats, vehicle_model, vehicle_number, destination):
        try:
            new_ride = Ride(user_name, origin, destination, available_seats, vehicle_number, vehicle_model)
            user = self.userManager.get_user(user_name)

            if not user.check_vehicle(vehicle_number):
                raise InvalidVehicle()

            self.rideManager.add_offer_ride(new_ride, user_name)
            
        except Exception as e:
            print(e)

    def select_ride(self, user_name, origin, destination, seats, strategy, vehicle):
        ride = None
        try:
            if strategy == SelectionStrategyType.PREFERRED:
                st = PreferredVehicleStrategy()
                ride = st.find_preferred_rides(origin, destination, seats, self.rideManager, vehicle)
            elif strategy == SelectionStrategyType.MOST_VACANT:
                st = MostVacantStrategy()
                ride = st.find_vacant_rides(origin, destination, seats, self.rideManager, vehicle)
            if ride:
                ride.add_passenger(user_name, seats)
            else:
                raise NoRideFound()
            
        except Exception as e:
            print(e)
        return ride

    def end_ride(self, user_name, origin, available_seats, vehicle_model, vehicle_number, destination):
        ride = self.rideManager.end_ride(vehicle_number)

        if ride is not None:
            ride.end_ride()
            shared_by = ride.get_shared_by()
            passengers = ride.get_selected_by()

            user = self.userManager.get_user(shared_by)
            user.add_shared_ride(ride)

            for s in passengers:
                user = self.userManager.get_user(s)
                user.add_consumed_ride(ride)


    def print_ride_status(self):
        users = self.userManager.get_users()
        for user in users:
            print(user.get_name() + ": " + str(len(user.get_consumed_rides())) + " Taken " + str(
                len(user.get_shared_rides())) + " Offered")


if __name__ == "__main__":
    app = Application()
    app.add_user("Rohan", 'M', 36)
    app.add_vehicle("Rohan", "Swift", "KA-01-12345")
    
    app.add_user("Shashank", 'M', 29)
    app.add_vehicle("Shashank", "Baleno", "TS-05-62395")
    
    app.add_user("Nandini", 'F', 29)
    
    app.add_user("Shipra", 'F', 27)
    app.add_vehicle("Shipra", "Polo", "KA-05-41491")
    app.add_vehicle("Shipra", "Activa", "KA-12-12332")
    
    app.add_user("Gaurav", 'M', 29)
    
    app.add_user("Rahul", 'M', 35)
    app.add_vehicle("Rahul", "XUV", "KA-05-1234")
    
    app.offer_ride("Rohan", "Hyderabad", 1, "Swift", "KA-01-12345", "Bangalore")
    app.offer_ride("Shipra", "Bangalore", 1, "Activa", "KA-12-12332", "Mysore")
    app.offer_ride("Shipra", "Bangalore", 2, "Polo", "KA-05-41491", "Mysore")
    app.offer_ride("Shashank", "Hyderabad", 2, "Baleno", "TS-05-62395", "Bangalore")
    app.offer_ride("Rahul", "Hyderabad", 5, "XUV", "KA-05-1234", "Bangalore")
    app.offer_ride("Rohan", "Bangalore", 1, "Swift", "KA-01-12345", "Pune")
    
    ride1 = app.select_ride("Nandini", "Bangalore", "Mysore", 1, SelectionStrategyType.MOST_VACANT, "None")
    ride2 = app.select_ride("Gaurav", "Bangalore", "Mysore", 1, SelectionStrategyType.PREFERRED, "Activa")
    ride3 = app.select_ride("Rohan", "Mumbai", "Bangalore", 1, SelectionStrategyType.PREFERRED, "Baleno")
    ride4 = app.select_ride("Rohan", "Hyderabad", "Bangalore", 1, SelectionStrategyType.PREFERRED, "Baleno")
    ride5 = app.select_ride("Shashank", "Hyderabad", "Bangalore", 1, SelectionStrategyType.PREFERRED, "Polo")
    
    app.end_ride("Rohan", "Hyderabad", 1, "Swift", "KA-01-12345", "Bangalore")
    app.end_ride("Shipra", "Bangalore", 1, "Activa", "KA-12-12332", "Mysore")
    app.end_ride("Shipra", "Bangalore", 2, "Polo", "KA-05-41491", "Mysore")
    app.end_ride("Shashank", "Hyderabad", 2, "Baleno", "TS-05-62395", "Bangalore")
    
    app.print_ride_status()
