from django.http import HttpResponse
from django.shortcuts import render

data = {
     'movies': [
         {
           'id' : 12,
           'title' : 'kanthara',
           'description' : 'story',
         },

         {
           'id' : 23,
           'title' : 'kanthara',
           'description' : 'story',
         },

         {
             'id' : 14,
           'title' : 'kanthara',
           'description' : 'story',
         },

         {
             'id' : 67,
           'title' : 'kanthara',
           'description' : 'story',
         }
         
    ]
} 

def movies(request):
    return render(request, 'movies/movies.html', data)

def home(request):
    return HttpResponse("Home page")
 