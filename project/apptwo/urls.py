from django.urls import path
from apptwo import views

urlpatterns = [
    path('', views.getUser, name='get_user'),
    path('register',views.register_user, name='register_user')
]