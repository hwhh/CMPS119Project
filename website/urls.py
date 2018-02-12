from django.conf.urls import url, include

from . import views

app_name = 'website'
urlpatterns = [
    url('^$', views.Landing.as_view()),
]
