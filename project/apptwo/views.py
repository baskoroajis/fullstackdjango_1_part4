from django.shortcuts import render
from apptwo.models import User
from django.http import HttpResponse
# Create your views here.

def getUser(request):
    user_list = User.objects.order_by('first_name')
    data = {'user_data' : user_list}
    return  render(request, 'apptwo/User.Html', context=data)

