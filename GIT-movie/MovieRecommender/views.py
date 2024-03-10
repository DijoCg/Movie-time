from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from math import ceil
from .forms import SignUpForm, AddMovieForm, LoginForm, UserProfileForm
from .models import Movie, UserProfile






def filterMovieByGenre():
    allMovies = []
    genresMovie = Movie.objects.values('genres', 'id')
    genres = {item["genres"] for item in genresMovie}
    for genre in genres:
        movie = Movie.objects.filter(genres=genre)
        n = len(movie)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allMovies.append([movie, range(1, nSlides), nSlides])
    params = {'allMovies': allMovies}
    return params


@login_required
def addmovie(request):
    if request.method == 'POST':
        form = AddMovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user  # Set the current user as the owner of the movie
            movie.save()
            messages.success(request, 'Movie added successfully.')
            return HttpResponseRedirect('/dashboard/')  # Redirect to dashboard after adding movie
    else:
        form = AddMovieForm()
    return render(request, 'MovieRecommender/addmovie.html', {'form': form})



def userlogin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = LoginForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully!!')
                    return HttpResponseRedirect('/dashboard/')
        else:
            fm = LoginForm()
        return render(request, 'MovieRecommender/login.html', {'form': fm})
    else:
        return HttpResponseRedirect('/dashboard/')


def home(request):
    params = filterMovieByGenre()
    return render(request, 'MovieRecommender/home.html', params)


def dashboard(request):
    if request.user.is_authenticated:
        params = filterMovieByGenre()
        params['user'] = request.user
        return render(request, 'MovieRecommender/dashboard.html', params)
    else:
        return HttpResponseRedirect('/login/')


def userlogout(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect('/login/')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful.')
            return HttpResponseRedirect('/login/')
    else:
        form = SignUpForm()
    return render(request, 'MovieRecommender/signup.html', {'form': form})


def profile(request):
    if request.user.is_authenticated:
        ratings = Rating.objects.filter(user=request.user)
        total_review = sum([int(rating.rating) for rating in ratings])
        total_watched_movie = ratings.count()
        return render(request, 'MovieRecommender/profile.html')
    else:
        return HttpResponseRedirect('/login/')






@login_required
def profile(request):
    user_profile = UserProfile.objects.get_or_create(user=request.user)[0]

    if request.method == 'POST':
        if 'profile_picture' in request.FILES:  # Check if a profile picture is being uploaded
            user_profile.profile_picture = request.FILES['profile_picture']
            user_profile.save()
            return HttpResponseRedirect('/profile/')  # Redirect to profile after updating profile picture
        else:
            form = UserProfileForm(request.POST, instance=user_profile)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/profile/')  # Redirect to profile after updating bio
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'MovieRecommender/profile.html', {'form': form})


@login_required
def edit_profile(request):
    user_profile = UserProfile.objects.get_or_create(user=request.user)[0]
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/profile/')  # Redirect to profile after updating
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'MovieRecommender/edit_profile.html', {'form': form})




