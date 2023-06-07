# Elevator System API

This API provides functionality for managing an elevator system.

## Endpoints

### 1. Initialize Elevator System

URL: `/api/initialize/`
Method: POST

* This endpoint initializes the elevator system by providing the number of elevators and the number of floors. It creates the elevator system instance and stores it in the cache for future use.
* To initialize the elevator system we have to pass two arguments (num_elevators: number of elevator in system) and (num_floors: no.of foors in building).
* You have to pass json for initializing the elevator system eg: {"num_elevators":5,"num_floors":10} .

### 2. Fetch All Requests

URL: `/api/requests/`
Method: GET

This endpoint retrieves all the current elevator requests in the system. It returns a JSON response containing the list of requests.

### 3. Add Request

URL: `/api/elevator/addrequest/<floor_no>/`
Method: GET

This endpoint adds a new request for a specific floor in the elevator system. It takes the floor number as a parameter and adds the request to the system.

### 4. Fetch Next Destination

URL: `/api/elevator/next_destination/`
Method: GET

This endpoint retrieves the next destination floor request which assigned for a specific elevator.

### 5. Check Elevator Direction

URL: `/api/elevator/direction/<int:elevator_id>/`
Method: GET

This endpoint check the direction of a specific elevator. It takes the elevator ID as a parameter and return the status dict, where one of value is direction.

### 6. Save User Request

URL: `/api/elevator/requests/<int:elevator_id>/`
Method: GET

* This endpoint adds a user request to a elevator system. It takes the floor number as a request payload, and adds the request to the elevator System.
* for e.g we want to request a lift on floor 5, then we use this url to request elevator to come by passing floor number.

### 7. Mark Elevator Not Working

URL: `/api/elevator/mark_not_working/<int:elevator_id>/`
Method: PUT

This endpoint marks a specific elevator as not working. It takes the elevator ID as a parameter and updates the elevator's status to not working.

### 8. Open/close Elevator Door

URL: `/api/elevator/door/<str:door>/<int:elevator_id>/`
Method: GET

This endpoint opens/close the door of a specific elevator. It takes the elevator ID as a parameter and string(open or close ) and according to string passed it updates the elevator's door status.

