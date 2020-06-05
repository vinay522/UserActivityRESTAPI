# Python script to populate fake data to the database using faker package
# pip install faker

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','UserActivityRESTAPI.settings')

import django
django.setup()

from faker import Faker 
from rest_api_demo_app.models import User, ActivityPeriod

fake = Faker()

def populate(N=5):
	for entry in range(N):
		fake_id = fake.pystr(min_chars=8, max_chars=10)
		fake_real_name = fake.name()
		fake_tz = fake.date_time()
		user_info = User.objects.get_or_create(id=fake_id, real_name=fake_real_name, tz=fake_tz)[0]

	for entry in range(N):
		fake_start_time = fake.date_time()
		fake_end_time = fake.date_time()
		user_info = ActivityPeriod.objects.get_or_create(start_time=fake_start_time, end_time=fake_end_time)[0]


if __name__ == '__main__':
	print("Populating databse with fake data")
	populate(20)
	print("Populated!!!")