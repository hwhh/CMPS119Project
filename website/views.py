from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic


# Create your views here.
class Landing(generic.View):
    def get(self, request):
        return render(request, 'website/pages/landing.html')
