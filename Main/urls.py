from django.urls import path

from .views import (
    InitializeElevatorSystemView,
    FetchAllRequestsView,
    FetchNextDestinationView,
    FetchElevatorDirectionView,
    MarkElevatorNotWorkingView,
    ElevatorDoorView,
    AddRequestView,
    GetRequestsOfElevatorView,
    AssignNextRequest,
)

urlpatterns = [
    path('initialize/', InitializeElevatorSystemView.as_view(), name='initialize'),
    path('assignnextrequest/', AssignNextRequest.as_view(), name='assign_elevator'),
    path('elevator/requests/', FetchAllRequestsView.as_view(), name='fetch_requests'),
    path('elevator/addrequest/<int:floor_no>/', AddRequestView.as_view(), name='add_request'),
    path('elevator/<int:elevator_id>/requests/', GetRequestsOfElevatorView.as_view(), name='fetch_requests_elevator'),
    path('elevator/next_destination/', FetchNextDestinationView.as_view(), name='next_destination'),
    path('elevator/<int:elevator_id>/direction/', FetchElevatorDirectionView.as_view(), name='elevator_direction'),
    path('elevator/<int:elevator_id>/mark_not_working/', MarkElevatorNotWorkingView.as_view(), name='mark_not_working'),
    path('elevator/open_door/<str:door>/<int:elevator_id>/', ElevatorDoorView.as_view(), name='open_door'),
]
