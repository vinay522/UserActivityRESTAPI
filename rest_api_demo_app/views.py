from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics
from rest_framework import mixins

# Create your views here.

#Generic View with GET, POST, PUT, DELETE requests for RESTAPI

class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, 
					mixins.CreateModelMixin, mixins.UpdateModelMixin,
					mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
	serializer_class = UserSerializer
	queryset = User.objects.all()

	lookup_field = 'id'

	def get(self, request, id=None):
		if id:
			return self.retrieve(request)
		else:
			return self.list(request)

	def post(self, request):
		return self.create(request)

	def put(self, request, id=None):
		return self.update(request, id)

	def delete(self, request, id):
		return self.destroy(request, id)



#Class Based View with GET, POST, PUT, DELETE requests for RESTAPI
class UserAPIView(APIView):

	def get(self, get):
		users = User.objects.all()
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = UserSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Class Based View with GET, POST, PUT, DELETE requests for RESTAPI
class UserDetails(APIView):

	def get_object(self, id):
		try:
			return User.objects.get(id=id)
		except User.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

	def get(self, request, id):
		user = self.get_object(id)
		serializer = UserSerializer(user)
		return Response(serializer.data)

	def put(self, request, id):
		user = self.get_object(id)
		serializer = UserSerializer(user, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, id):
		user = self.get_object(id)
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
