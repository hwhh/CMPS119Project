from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, '../templates/index.html', context)


def about(request):
    context = {}
    return render(request, '../templates/about.html', context)


def work(request):
    context = {}
    return render(request, '../templates/work.html', context)


def blog(request):
    context = {}
    return render(request,'../templates/blog.html', context)


def contact(request):
    context = {}
    return render(request, '../templates/contact.html', context)
