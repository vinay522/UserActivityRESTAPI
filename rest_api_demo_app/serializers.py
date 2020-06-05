from rest_framework import serializers
from .models import User, ActivityPeriod


# Serializer class for Activity Period to get start_time and end_time as JSON data
class ActivityPeriodSerializer(serializers.ModelSerializer):
	class Meta:
		model = ActivityPeriod
		fields = ['start_time', 'end_time']


# Serializer class for User Period to get all fields as JSON data
class UserSerializer(serializers.ModelSerializer):
	activity_periods = ActivityPeriodSerializer()
	class Meta:
		model = User
		fields = ['id', 'real_name', 'tz', 'activity_periods']
