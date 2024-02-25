class AlreadyRideExists(Exception):
    def __init__(self):
        super().__init__("Ride already exists")

class InvalidUser(Exception):
    def __init__(self):
        super().__init__("Invalid User")
        
class InvalidVehicle(Exception):
    def __init__(self):
        super().__init__("Invalid Vehicle")

class NoRideFound(Exception):
    def __init__(self):
        super().__init__("No Ride Found")

class UserAlreadyExists(Exception):
    def __init__(self):
        super().__init__("User already exists")

class VehicleAlreadyExists(Exception):
    def __init__(self):
        super().__init__("Vehicle already exists")
