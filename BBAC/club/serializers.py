from rest_framework import serializers
from .models import *


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    created_by = MemberSerializer(read_only = True) # nested data
    class Meta:
        model = Event
        fields = '__all__'

class ParticipationSerializer(serializers.ModelSerializer):
    member = MemberSerializer(read_only=True)
    event = EventSerializer(read_only = True)

    class Meta:
        model = Participation
        fields = '__all__'