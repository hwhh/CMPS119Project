from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mission', views.mission, name='mission'),
    path('volunteers', views.volunteers, name='volunteers'),
    path('systems', views.systems, name='systems'),

]