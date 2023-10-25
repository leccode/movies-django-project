from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie, Soundtrack

def movies(request):
    data = Movie.objects.all()
    return render(request, "movies/movies.html", {"movies": data})

def soundtracks(request):
    data = Soundtrack.objects.all()
    return render(request, "movies/soundtracks.html", {"soundtracks": data})

def home(request):
    return HttpResponse("Home page")