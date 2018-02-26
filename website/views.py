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

#system_photo route
def system_photo(request):
	context = {}
	return render(request, '../templates/system_photo.html', context)

#about system route
def about(request):
	context = {}
	return render(request, '../templates/about.html', context)


#request site survey route
def request_site_survey(request):
	context = {}
	return render(request, '../templates/request_site_survey.html', context)

#get started route
def getting_started(request):
	context = {}
	return render(request, '../templates/getting_started.html', context)

#documents route
def documents(request):
	context = {}
	return render(request, '../templates/documents.html', context)

#team route
def team(request):
	context = {}
	return render(request, '../templates/team.html', context)


#team directors route
def directors(request):
	context = {}
	return render(request, '../templates/directors.html', context)

def handler404(request, exception, template_name='404.html'):
	return render(request, '../templates/404.html', {})

def handler500(request, exception, template_name='404.html'):
	return render(request, '../templates/500.html', {})