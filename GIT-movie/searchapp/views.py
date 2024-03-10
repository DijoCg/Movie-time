from django.shortcuts import render
from django.db.models import Q
from MovieRecommender.models import Movie


def SearchResult(request):
    movies = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        if query:
            movies = Movie.objects.filter(Q(title__icontains=query) | Q(genres__icontains=query))
    return render(request, 'MovieRecommender/search.html', {'query': query, 'movies': movies})
