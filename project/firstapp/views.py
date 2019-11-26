from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#
def get_index_view(request):
    return HttpResponse('<em> My Second App <em>')

def get_help(request):
    dict_val = {'help_val' : "Help page !!!!!"}
    return render(request, 'firstapp/Help.html', context=dict_val)