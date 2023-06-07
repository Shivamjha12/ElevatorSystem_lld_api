# Elevator System API

This API provides functionality for managing an elevator system.

## Endpoints

### 1. Initialize Elevator System

URL: `/api/initialize/`
Method: POST

This endpoint initializes the elevator system by providing the number of elevators and the number of floors. It creates the elevator system instance and stores it in the cache for future use.

### 2. Fetch All Requests

URL: `/api/requests/`
Method: GET

This endpoint retrieves all the current elevator requests in the system. It returns a JSON response containing the list of requests.

### 3. Add Request

URL: `/api/elevator/addrequest/<floor_no>/`
Method: GET

This endpoint adds a new request for a specific floor in the elevator system. It takes the floor number as a parameter and adds the request to the system.

### 4. Fetch Next Destination

URL: `/api/elevator/<elevator_id>/nextdestination/`
Method: GET

This endpoint retrieves the next destination floor for a specific elevator. It takes the elevator ID as a parameter and returns the next destination floor in the response.

### 5. Fetch Elevator Direction

URL: `/api/elevator/<elevator_id>/direction/`
Method: GET

This endpoint retrieves the current direction of a specific elevator. It takes the elevator ID as a parameter and returns the direction (up, down, or stationary) in the response.

### 6. Save User Request

URL: `/api/elevator/<elevator_id>/addrequest/`
Method: POST

This endpoint adds a user request to a specific elevator. It takes the elevator ID as a parameter and the floor number as a request payload, and adds the request to the elevator.

### 7. Mark Elevator Not Working

URL: `/api/elevator/<elevator_id>/notworking/`
Method: PUT

This endpoint marks a specific elevator as not working. It takes the elevator ID as a parameter and updates the elevator's status to not working.

### 8. Open Elevator Door

URL: `/api/elevator/<elevator_id>/opendoor/`
Method: PUT

This endpoint opens the door of a specific elevator. It takes the elevator ID as a parameter and updates the elevator's door status to open.

### 9. Close Elevator Door

URL: `/api/elevator/<elevator_id>/closedoor/`
Method: PUT

This endpoint closes the door of a specific elevator. It takes the elevator ID as a parameter and updates the elevator's door status to closed.

