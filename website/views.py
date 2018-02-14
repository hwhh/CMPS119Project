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

#systems route
def systems(request):
	context = {}
	return render(request, '../templates/systems.html', context)

#sunthink route
def sunthink(request):
	context = {}
	return render(request, '../templates/sunthink.html', context)

#sunthinkAbout route
def sunthinkabout(request):
	context = {}
	return render(request, '../templates/sunthinkabout.html', context)

#sunthinkHowTo route
def sunthinkhowto(request):
	context = {}
	return render(request, '../templates/sunthinkhowto.html', context)

#events route
def events(request):
	context = {}
	return render(request, '../templates/events.html', context)

#news route
def news(request):
	context = {}
	return render(request, '../templates/news.html', context)

#newsletter route
def newsletter(request):
	context = {}
	return render(request, '../templates/newsletter.html', context)