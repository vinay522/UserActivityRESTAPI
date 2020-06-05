from django.db import models
from django.utils import timezone

# Create your models here.

#User Model with required fields
class User(models.Model):
	id = models.CharField(max_length=50, primary_key=True)
	real_name = models.CharField(max_length=200)
	tz = models.DateTimeField(default=timezone.now)
	activity_periods = models.ForeignKey('ActivityPeriod', null=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.real_name


#ActivityPeriod Model with start_time and end_time fields
class ActivityPeriod(models.Model):
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()

	def __str__(self):
		return "{}".format(self.start_time)
