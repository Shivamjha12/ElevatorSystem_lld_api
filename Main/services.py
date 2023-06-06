from queue import Queue

class Elevator:
    def __init__(self, elevator_id, top_floor):
        self.id = elevator_id
        self.current_floor = 0
        self.direction = "idle"
        self.is_running = False
        self.is_door_open = False
        self.top_floor = top_floor
        self.requested_floors = []
        self.is_working = True
        
    def mark_is_working(self,assign_val):
        self.is_working = assign_val
        return self.is_working
    
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
        status = {
            f"Current_floor": self.current_floor,
            "Direction":self.direction,
            "Is Running":self.is_running,
            "Is Door Open":self.is_door_open
        }
        return status
        # print(f"Elevator {self.id} is at floor {self.current_floor}.")
        # print(f"Direction: {self.direction}")
        # print(f"Running status: {'Running' if self.is_running else 'Stopped'}")
        # print(f"Door status: {'Open' if self.is_door_open else 'Closed'}")


class ElevatorSystem:
    def __init__(self, num_elevators, num_floors):
        self.elevators = [Elevator(i, num_floors - 1) for i in range(num_elevators)]
        self.num_floors = num_floors
    
    def get_optimal_elevator(self,floor):
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
        return optimal_elevator
    
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
            optimal_elevator.requested_floors.append(floor)
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
        
    def get_all_elevator_status(self):
        for i in self.elevators:
            print(self.display_elevator_status(i.id))
    
    def get_elevator_requests(self, elevator_id):
        if elevator_id < len(self.elevators):
            return self.elevators[elevator_id].requested_floors
        else:
            print(f"Elevator {elevator_id} does not exist")
        
    def display_elevator_status(self, elevator_id):
        if elevator_id < len(self.elevators):
            return self.elevators[elevator_id].display_status()
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
        self.num_floors = num_floors
        self.elevator_system = ElevatorSystem(num_elevators, num_floors)
        self.floors = [Floor(i, self) for i in range(num_floors)]
        self.requests = []
        # Queue()
        
    def next_destination(self):
        if len(self.requests)>=1:
            return self.requests[0]
        return -1
    
    def current_requests(self):
        return self.requests

    def add(self,request):
        if request < self.num_floors:
            self.requests.append(request)
            return f'The request of adding {request} values to requests queue is successfully'
        return f'Invalid request {request} floor value is greater than {self.num_floors} floor value which is top floor'
    
    def assign_elevator(self):
        floor_no = self.requests[0]
        self.requests.pop(0)
        # self.requests.task_done()
        floor = self.floors[floor_no]
        return self.elevator_system.assign_elevator(floor.floor_no)

# 1
# building = Building(num_elevators=2, num_floors=10)
# building.add(6)
# building.add(1)
# building.add(8)
# print(building.next_destination())
# building.assign_elevator()
# building.elevator_system.get_all_elevator_status()

# 2
# print(building.current_requests())
# building.assign_elevator()
# print(building.current_requests()[0])
# building.assign_elevator()
# print(req)

# new example
# building = Building(num_elevators=2, num_floors=10)
# req1 = building.floors[6]
# building.elevator_system.display_elevator_status(0)
# elevator = req1.request_elevator()
# print(elevator)
# building.elevator_system.display_elevator_status(elevator)
# floor2 = building.floors[1]
# floor2.request_elevator()

# 3
# elevator_system = ElevatorSystem(num_elevators=2, num_floors=10)
# elevator = elevator_system.assign_elevator(9)
# elevator = elevator_system.assign_elevator(4)
# elevator = elevator_system.assign_elevator(8)
# elevator = elevator_system.assign_elevator(9)
# elevator = elevator_system.assign_elevator(1)
# elevator = elevator_system.assign_elevator(9)
# elevator_system.display_elevator_status(elevator)