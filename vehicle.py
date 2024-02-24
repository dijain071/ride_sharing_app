class Vehicle:
    def __init__(self, user_name, model, vehicle_number):
        self.user_name = user_name
        self.model = model
        self.vehicle_number = vehicle_number

    def get_user_name(self):
        return self.user_name

    def set_user_name(self, user_name):
        self.user_name = user_name

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def get_vehicle_number(self):
        return self.vehicle_number

    def set_vehicle_number(self, vehicle_number):
        self.vehicle_number = vehicle_number
