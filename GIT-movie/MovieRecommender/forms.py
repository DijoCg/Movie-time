from django import forms
from django.contrib.auth.models import User
from .models import Movie
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserProfile

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'first_name': 'First Name', 'last_name': 'Last Name', 'email': 'Email Address'}
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class AddMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ['user']
        labels = {'title': 'Movie Title', 'image': 'Poster', 'movieduration': 'Duration','trailerlink':'trailerlink'}
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter movie title'}),
            'genres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter movie genres'}),
            'year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter movie release year'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'movieduration': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter movie duration'}),
            'trailerlink': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter movie Trailer link'}),
        }

    def clean_year(self):
        year = self.cleaned_data['year']
        try:
            year = int(year)
        except ValueError:
            raise forms.ValidationError("Please enter a valid year.")
        return year

    def clean_image(self):
        image = self.cleaned_data['image']
        if image:
            if not image.content_type.startswith('image'):
                raise forms.ValidationError("File is not an image.")
        return image

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        fields = ['username', 'password']





class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'bio']

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['profile_picture'].widget.attrs['class'] = 'custom-file-input'