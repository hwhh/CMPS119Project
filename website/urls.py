from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mission', views.mission, name='mission'),
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
    path('getting_started', views.getting_started, name='getting_started'),
    path('documents', views.documents, name='documents'),
    path('team', views.team, name='team'),
    path('map', views.sunwork_map, name='map'),
    path('volunteers', views.volunteers, name='volunteers'),
    path('new_volunteers', views.new_volunteers, name='new_volunteers'),
    path('existing_volunteers', views.existing_volunteers, name='existing_volunteers'),
    path('systems/nonprofit', views.nonprofit, name='nonprofit'),
    path('systems/cases', views.cases, name='cases'),
    path('mission/objectives', views.objectives, name='objectives'),
    path('mission/support', views.support, name='support'),
    path('mission/philosophy', views.philosophy, name='philosophy'),
    path('systems/netmetering', views.netmetering, name='netmetering'),
    path('systems/nem2', views.nem2, name='nem2'),


    path('contact/', views.contact, name='contact'),
]