class Elevator:
    def __init__(self, elevator_id, top_floor):
        self.id = elevator_id
        self.current_floor = 0
        self.direction = "idle"
        self.is_running = False
        self.is_door_open = False
        self.top_floor = top_floor

    def move_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
        self.direction = "Up"

    def move_down(self):
        if self.current_floor > 0:
            self.current_floor -= 1
        self.direction = "Down"

    def open_door(self):
        self.is_door_open = True

    def close_door(self):
        self.is_door_open = False

    def start(self):
        self.is_running = True

    def stop(self):
        self.is_running = False

    def display_status(self):
        print(f"Elevator {self.id} is at floor {self.current_floor}.")
        print(f"Direction: {self.direction}")
        print(f"Running status: {'Running' if self.is_running else 'Stopped'}")
        print(f"Door status: {'Open' if self.is_door_open else 'Closed'}")


class ElevatorSystem:
    def __init__(self, num_elevators, num_floors):
        self.elevators = [Elevator(i, num_floors - 1) for i in range(num_elevators)]
        self.num_floors = num_floors

    def assign_elevator(self, floor):
        if floor < 0 or floor >= self.num_floors:
            return f"Invalid floor number. Please provide a floor between 0 and {self.num_floors - 1}."

        # Find the most optimal elevator based on distance and availability
        optimal_elevator = None
        min_distance = float('inf')
        for elevator in self.elevators:
            distance = abs(elevator.current_floor - floor)
            if not elevator.is_running and distance < min_distance:
                optimal_elevator = elevator
                min_distance = distance

        if optimal_elevator is not None:
            optimal_elevator.start()

            while optimal_elevator.current_floor != floor:
                if optimal_elevator.current_floor < floor:
                    optimal_elevator.move_up()
                elif optimal_elevator.current_floor > floor:
                    optimal_elevator.move_down()

            optimal_elevator.stop()
            print(f"Elevator {optimal_elevator.id} is assigned to floor {floor}")
            return optimal_elevator.id
        else:
            return "No available elevator to assign", None

    def mark_elevator_not_working(self, elevator_id):
        if elevator_id < len(self.elevators):
            self.elevators[elevator_id].stop()
            return f"Elevator {elevator_id} is marked as not working"
        else:
            return f"Elevator {elevator_id} does not exist"

    def open_elevator_door(self, elevator_id):
        if elevator_id < len(self.elevators):
            self.elevators[elevator_id].open_door()
            return f"Door of elevator {elevator_id} is opened"
        else:
            return f"Elevator {elevator_id} does not exist"

    def close_elevator_door(self, elevator_id):
        if elevator_id < len(self.elevators):
            self.elevators[elevator_id].close_door()
            return f"Door of elevator {elevator_id} is closed"
        else:
            return f"Elevator {elevator_id} does not exist"

    def display_elevator_status(self, elevator_id):
        if elevator_id < len(self.elevators):
            self.elevators[elevator_id].display_status()
        else:
            print(f"Elevator {elevator_id} does not exist")

class Floor:
    def __init__(self, floor_no, building):
        self.floor_no = floor_no
        self.building = building

    def request_elevator(self):
        assigned_elevator = self.building.assign_elevator(self.floor_no)
        if assigned_elevator is not None:
            # print(f"Elevator {assigned_elevator} has been assigned to Floor {self.floor_no}")
            return assigned_elevator
        else:
            print(f"No available elevator to assign to Floor {self.floor_no}")


class Building:
    def __init__(self, num_elevators, num_floors):
        self.elevator_system = ElevatorSystem(num_elevators, num_floors)
        self.floors = [Floor(i, self) for i in range(num_floors)]

    def assign_elevator(self, floor):
        return self.elevator_system.assign_elevator(floor)
    