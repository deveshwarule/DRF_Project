from django.shortcuts import render
from APP.models import Movie
from django.http import JsonResponse

# Create your views here.
def movies_list(request):
    movies = Movie.objects.all()
    data = {
        'Movie': list(movies.values())
        }
    return JsonResponse(data)

def movies_details(request,pk):
    movie = Movie.objects.get(pk=pk)
    data={
        'Movie': movie.name,
        'Description': movie.description,
        'Status': movie.active
    }
    return JsonResponse(data)