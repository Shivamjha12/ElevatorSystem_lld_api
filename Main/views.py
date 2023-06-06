from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .services import Building
from django.core.cache import cache

building = None

class InitializeElevatorSystemView(APIView):
    def post(self, request):
        global building
        num_elevators = request.data.get('num_elevators')
        num_floors = request.data.get('num_floors')
        building = Building(num_elevators, num_floors)
        cache.set('building_instance', building)
        print(building.current_requests())
        return Response(status=status.HTTP_200_OK)
class AssignNextRequest(APIView):
    def get(self, request):
        building.assign_elevator()
        return Response(status=status.HTTP_200_OK)

class FetchAllRequestsView(APIView):
    def get(self, request):
        elevator_requests = building.current_requests()
        print(elevator_requests)
        response_data = {
            'message': "all request we have in queue",
            'requests': elevator_requests,
        }
        
        return JsonResponse(response_data, status=status.HTTP_200_OK)
    
class AddRequestView(APIView):
    def get(self,requests,floor_no):
        building.add(floor_no)
        response_data ={
            "message": f"Request for floor no {floor_no} is added"
        }
        return JsonResponse(response_data, status=status.HTTP_200_OK)
class GetRequestsOfElevatorView(APIView):
    def get(self,requests,elevator_id):
        pass
        all_past_requests = building.elevator_system.get_elevator_requests(elevator_id)
        elevator_status = building.elevator_system.display_elevator_status(elevator_id)
        response_data ={
            "message": f"All past requests get by elevator {elevator_id}",
            "requests": all_past_requests,
            "status":elevator_status
        }
        return JsonResponse(response_data, status=status.HTTP_200_OK)
    
class FetchNextDestinationView(APIView):
    def get(self, request):
        next_floor = building.next_destination()
        if next_floor==-1:
            response_data={
            "Message": f'Currently there is no requests'
            }
            return Response(response_data, status=status.HTTP_200_OK)
        next_destination = building.elevator_system.get_optimal_elevator(next_floor)
        response_data={
            "Explanataion: next destination": f' The next floor is {next_floor} and elevator->{next_destination.id} is assigned to it'
        }
        return Response(response_data, status=status.HTTP_200_OK)


class FetchElevatorDirectionView(APIView):
    def get(self, request, elevator_id):
        elevator_status=building.elevator_system.elevators[elevator_id].display_status()
        return Response({'direction': elevator_status["Direction"]}, status=status.HTTP_200_OK)


class MarkElevatorNotWorkingView(APIView):
    def post(self, request, elevator_id):
        building.elevator_system.elevators[elevator_id].mark_is_working(False)
        return Response(status=status.HTTP_200_OK)


class ElevatorDoorView(APIView):
    def get(self, request, door,elevator_id):
        print(door)
        if str(door)=="open": 
            building.elevator_system.elevators[elevator_id].open_door()
            return Response({"message":f'Now door is opened for elevator id {elevator_id}'},status=status.HTTP_200_OK)
        elif door=="close":
            building.elevator_system.elevators[elevator_id].close_door()
            return Response({"message":f'Now door is Closed for elevator id {elevator_id}'},status=status.HTTP_200_OK)
