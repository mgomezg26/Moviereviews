from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    #return HttpResponse('<h1>Welcome to Jungle</h1>')
    return render(request, 'home.html', {'name': 'Greg lim'})
def about(request):
    return HttpResponse('<h1>Hola Mundo</h1>')