class vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

veh = vehicle(240, 18)
print("Max_speed is",veh.max_speed,"Mileage is",veh.mileage)