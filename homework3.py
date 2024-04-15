class Vehicle:
    def __init__(self, brand, license_plate):
        self.brand = brand
        self.license_plate = license_plate

    def get_brand(self):
        return self.brand

    def set_brand(self, brand):
        self.brand = brand

    def get_license_plate(self):
        return self.license_plate

    def set_license_plate(self, license_plate):
        self.license_plate = license_plate


class Car(Vehicle):
    def __init__(self, brand, license_plate, body_type):
        super().__init__(brand, license_plate)
        self.body_type = body_type

    def get_body_type(self):
        return self.body_type

    def set_body_type(self, body_type):
        self.body_type = body_type


class ParkingLot:
    def __init__(self, capacity):
        self.vehicles = []
        self.capacity = capacity

    def get_capacity(self):
        return self.capacity

    def set_capacity(self, capacity):
        self.capacity = capacity

    def add_vehicle(self, vehicle):
        if len(self.vehicles) < self.capacity:
            self.vehicles.append(vehicle)
            print(f"{vehicle.get_brand()} with license plate {vehicle.get_license_plate()} has been parked.")
        else:
            print("Parking lot is full.")

    def remove_vehicle(self, license_plate):
        for vehicle in self.vehicles:
            if vehicle.get_license_plate() == license_plate:
                self.vehicles.remove(vehicle)
                print(f"Vehicle with license plate {license_plate} has left the parking lot.")
                return
        print(f"Vehicle with license plate {license_plate} is not found in the parking lot.")

    def get_free_spaces(self):
        return self.capacity - len(self.vehicles)

    def get_all_vehicles(self):
        return [vehicle.get_brand() + " - " + vehicle.get_license_plate() for vehicle in self.vehicles]

car1 = Car("Toyota", "ABC123", "Sedan")
car2 = Car("Honda", "XYZ789", "Hatchback")

parking_lot = ParkingLot(5)
parking_lot.add_vehicle(car1)
parking_lot.add_vehicle(car2)

print(parking_lot.get_free_spaces())  # Output: 3

parking_lot.remove_vehicle("ABC123")  # Output: Vehicle with license plate ABC123 has left the parking lot.

print(parking_lot.get_all_vehicles())  # Output: ['Honda - XYZ789']