from django.shortcuts import render

# index route
def index(request):
    context = {}
    return render(request, '../templates/index.html', context)


#mission route
def mission(request):
	context = {}
	return render(request, '../templates/mission.html', context)

#volunteers route
def volunteers(request):
	context = {}
	return render(request, '../templates/volunteers.html', context)
