from django.shortcuts import render
from apptwo.models import User
from django.http import HttpResponse
from apptwo.forms import  NewUserForm
# Create your views here.

def getUser(request):
    user_list = User.objects.order_by('first_name')
    data = {'user_data' : user_list}
    return  render(request, 'apptwo/User.Html', context=data)

def register_user(request):
    form = NewUserForm()

    if (request.method == 'POST'):
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse('sukses register new user')

    return render(request, 'apptwo/register_form.html', context={'form' : form})

