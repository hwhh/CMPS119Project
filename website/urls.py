from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mission', views.mission, name='mission'),
    path('volunteers', views.volunteers, name='volunteers'),
    path('systems', views.systems, name='systems'),
    path('sunthink', views.sunthink, name='sunthink'),
    path('sunthink/sunthinkabout', views.sunthinkabout, name='sunthinkabout'),
    path('sunthink/sunthinkhowto', views.sunthinkhowto, name='sunthinkhowto'),
    path('events', views.events, name='events'),
    path('events/news', views.news, name='news'),
    path('events/newsletter', views.newsletter, name='newsletter'),
    path('systems/system_photo', views.system_photo, name='system_photo'),

]