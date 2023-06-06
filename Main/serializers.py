from rest_framework import serializers

class ElevatorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    current_floor = serializers.IntegerField()
    direction = serializers.CharField()
    is_running = serializers.BooleanField()
    is_door_open = serializers.BooleanField()
    top_floor = serializers.IntegerField()
