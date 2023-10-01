from enum import Enum

class Direction(Enum):
    UP = 1
    DOWN = -1

class Elevator:
    def __init__(self, num_floors):
        self.num_floors = num_floors
        self.current_floor = 1
        self.direction = Direction.UP
        self.requests = set()

    def move(self):
        if self.direction == Direction.UP:
            self.current_floor += 1
        else:
            self.current_floor -= 1

    def add_request(self, floor):
        self.requests.add(floor)

    def process_requests(self):
        while self.requests:
            if self.current_floor in self.requests:
                self.requests.remove(self.current_floor)
                print(f"Stopping at floor {self.current_floor}")
                # Open and close the doors, handle passengers
            self.move()

class ElevatorControlSystem:
    def __init__(self, num_elevators, num_floors):
        self.elevators = [Elevator(num_floors) for _ in range(num_elevators)]

    def request_elevator(self, floor, direction):
        min_distance = float('inf')
        nearest_elevator = None

        for elevator in self.elevators:
            if elevator.direction == Direction.UP and direction == Direction.UP and elevator.current_floor <= floor:
                distance = floor - elevator.current_floor
            elif elevator.direction == Direction.DOWN and direction == Direction.DOWN and elevator.current_floor >= floor:
                distance = elevator.current_floor - floor
            else:
                distance = abs(elevator.current_floor - floor)

            if distance < min_distance:
                min_distance = distance
                nearest_elevator = elevator

        if nearest_elevator:
            nearest_elevator.add_request(floor)
        else:
            print(f"No available elevators for request: floor {floor}, direction {direction}")

    def step(self):
        for elevator in self.elevators:
            elevator.process_requests()

# Example usage:
ecs = ElevatorControlSystem(num_elevators=2, num_floors=10)
ecs.request_elevator(5, Direction.UP)
ecs.request_elevator(3, Direction.DOWN)

# Simulate the passage of time and process elevator requests
for _ in range(20):
    ecs.step()
