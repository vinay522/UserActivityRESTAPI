from django.urls import path
from . import views


# URL patterns to access the class based views and Generic views
# http://127.0.0.1:8000/user/ - class based views
# http://127.0.0.1:8000/user/<id> - class based views

# http://127.0.0.1:8000/generic/user/ - Generic Views
# http://127.0.0.1:8000/generic/user/<id> - Generic based views

urlpatterns = [
    path('user/', views.UserAPIView.as_view(), name='user_list'),
    path('user/<id>/', views.UserDetails.as_view(), name='user_details'),
    path('generic/user/', views.GenericAPIView.as_view(), name='generic_user'),
    path('generic/user/<id>/', views.GenericAPIView.as_view(), name='generic_user_details'),
]
