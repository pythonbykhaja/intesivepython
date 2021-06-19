class Vehicle:
    def start_hire(self):
        print("hire started")

    def stop_hire(self):
        print("hire finished.")

class Bike(Vehicle):
    pass

vehicle = Vehicle()
vehicle.start_hire()
vehicle.stop_hire()

pulsar_bike = Bike()
pulsar_bike.start_hire()
pulsar_bike.stop_hire()


