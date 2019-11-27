from django.conf.urls import url
from firstapp import views

urlpatterns = [
    url(r'^$', views.get_help, name='help'),
    url(r'^bas', views.get_index_view, name='help2'),

]