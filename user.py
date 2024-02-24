from edge_cases import ( VehicleAlreadyExists)


class User:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        self.vehicles = []
        self.shared_rides = []
        self.consumed_rides = []

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_gender(self):
        return self.gender

    def set_gender(self, gender):
        self.gender = gender

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_vehicles(self):
        return self.vehicles

    def set_vehicles(self, vehicles):
        self.vehicles = vehicles

    def add_vehicle(self, vehicle):
        if vehicle in self.vehicles:
            raise VehicleAlreadyExists()
        self.vehicles.append(vehicle)

    def check_vehicle(self, vehicle_number):
        for vehicle in self.vehicles:
            if vehicle.get_vehicle_number() == vehicle_number:
                return True
        return False

    def get_shared_rides(self):
        return self.shared_rides

    def get_consumed_rides(self):
        return self.consumed_rides

    def add_consumed_ride(self, ride):
        self.consumed_rides.append(ride)

    def add_shared_ride(self, ride):
        self.shared_rides.append(ride)
