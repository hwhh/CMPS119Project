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
    path('systems/about', views.about, name='about'),
    path('request_site_survey', views.request_site_survey, name='request_site_survey'),
    path('index/getting_started', views.getting_started, name='getting_started'),
    path('index/documents', views.documents, name='documents'),
    path('team', views.team, name='team'),
    path('volunteers/new_volunteer', views.new_volunteer, name='new_volunteer'),
    path('systems/nonprofit', views.nonprofit, name='nonprofit'),
    path('mission/objectives', views.objectives, name='objectives'),


    path('contact/', views.contact, name='contact'),
]