from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie
# Create your views here.
def home(request):
    #return HttpResponse('<h1>Welcome to Jungle</h1>')
    #return render(request, 'home.html', {'name': 'Mateo Gomez'})

    searchterm = request.GET.get('searchMovie')
    if searchterm:
        movies = Movie.objects.filter(title__icontains=searchterm)
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html', {'movies': movies, 'searchterm': searchterm, 'name': 'Mateo Gomez'})

def about(request):
    #return HttpResponse('<h1>Hola Mundo</h1>')
    return render(request, 'about.html')