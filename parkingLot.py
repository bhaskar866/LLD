# - The parking lot should have multiple floors where customers can park their cars.
# - The parking lot should have multiple entry and exit points.
# - Customers can collect a parking ticket from the entry points and can pay the parking fee at the exit points to the parking attendant or automated exit panel
# - Customers can pay via both cash and credit cards.
# - The system should not allow more vehicles than the maximum capacity of the parking lot. If the parking is full, the system should be able to show a message at the entrance panel and on the parking display board on the ground floor.
# - Each parking floor will have many parking spots. The system should support multiple types of parking spots such as Compact, Large, Disabled, Motorcycle, etc.
# - The system should support parking for different types of vehicles like car, truck, van, motorcycle, etc.
# - Each parking floor should have a display board showing any free parking spot for each spot type.
# - The system should support a per-hour parking fee model. For example, customers have to pay some amount based on the Vehicle type.
# - Admins should be able to add parking floors and parking spot.

class ParkingSpot:
    def __init__(self, spot_type, floor_number):
        self.spot_type = spot_type
        self.is_occupied = False
        self.floor_number = floor_number

class ParkingFloor:
    def __init__(self, floor_number):
        self.floor_number = floor_number
        self.spots = []

    def add_spot(self, spot_type, num_spots):
        for _ in range(num_spots):
            self.spots.append(ParkingSpot(spot_type, self.floor_number))

class ParkingLot:
    def __init__(self, num_floors):
        self.num_floors = num_floors
        self.floors = []

    def add_floor(self):
        floor = ParkingFloor(len(self.floors) + 1)
        self.floors.append(floor)
        return floor


    def is_full(self):
        for floor in self.floors:
            for spot in floor.spots:
                if not spot.is_occupied:
                    return False
        return True

    def find_available_spot(self, spot_type):
        for floor in self.floors:
            for spot in floor.spots:
                if not spot.is_occupied and spot.spot_type == spot_type:
                    return spot
        return None

    def park_vehicle(self, vehicle_type):
        if self.is_full():
            return "Parking lot is full. Cannot park."

        spot_type = self.get_spot_type_for_vehicle(vehicle_type)
        available_spot = self.find_available_spot(spot_type)


        if available_spot:
            available_spot.is_occupied = True
            return f"Parking successful on floor {available_spot.floor_number}, spot type {spot_type}"
        else:
            return "No available spot of the requested type."

    def get_spot_type_for_vehicle(self, vehicle_type):
        # Implement logic to map vehicle types to spot types
        # This could be a dictionary or a more complex mapping based on your needs
        spot_type_mapping = {
            "car": "Compact",
            "truck": "Large",
            "van": "Large",
            "motorcycle": "Motorcycle",
        }
        return spot_type_mapping.get(vehicle_type, "Unknown")

# Example usage:
if __name__ == "__main__":
    parking_lot = ParkingLot(num_floors=3)

    # Add parking floors and spots
    for _ in range(3):
        floor = parking_lot.add_floor()

    # Add 10 compact spots per floor

    floor1, floor2, floor3 = parking_lot.floors

    floor1.add_spot("Compact", 10)
    floor2.add_spot("Motorcycle", 10)
    floor3.add_spot("Large", 10)

    # Park vehicles
    print(parking_lot.park_vehicle("car"))
    print(parking_lot.park_vehicle("motorcycle"))
    print(parking_lot.park_vehicle("truck"))
