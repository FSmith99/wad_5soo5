from django import forms
from rango.models import *
from django.contrib.auth.forms import UserCreationForm


class FilmForm(forms.ModelForm):

    YEARS = [x for x in range(1900,2020)]
    filmID = forms.CharField(widget = forms.HiddenInput(), required = False)
    title = forms.CharField(max_length = 128, help_text="Enter the film title.")
    director = forms.CharField(max_length = 128, help_text="Directors Name.")
    releaseDate = forms.DateField(help_text="Release Date.", widget=forms.SelectDateWidget(years=YEARS))
    blurb = forms.CharField(max_length = 512, help_text="Film Blurb.")
    poster = forms.ImageField(help_text="Film Poster.", required=False)
    slug = forms.SlugField(widget=forms.HiddenInput(), required = False)



    class Meta:
        model = Film
        fields=('title','director','releaseDate','blurb','poster')

class ReviewForm(forms.ModelForm):
    reviewerID = forms.CharField(widget=forms.HiddenInput(),required=False)
    fkID = forms.CharField(widget=forms.HiddenInput(),required=False)
    mainBody = forms.CharField(max_length = 1000, help_text="Review Body.")
    rating = forms.IntegerField(min_value = 0, max_value = 5, help_text="Rating 0-5")
    date = forms.DateTimeField(widget = forms.HiddenInput(), required = False)



    class Meta:
        model = Review
        exclude=('reviewerID','fkID','date')

class RatingForm(forms.ModelForm):
    userID = forms.CharField(widget=forms.HiddenInput(),required=False)
    fkID = forms.CharField(widget=forms.HiddenInput(),required=False)
    rating = forms.IntegerField(max_value = 5, min_value = 0,help_text="Score 0-5")

    class Meta:
        model = Rating
        fields = ('rating',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class ReviewerForm(forms.ModelForm):
    user = forms.ChoiceField(widget=forms.HiddenInput,required=False)
    displayName = forms.CharField(max_length=20, help_text="Enter your new display name.")
    profilePicture = forms.ImageField(required=False, help_text="Choose your profile picture.")
    slug = forms.CharField(widget=forms.HiddenInput(),required=False)
    date = forms.DateField(widget=forms.HiddenInput(),required=False)

    class Meta:
        model = Reviewer
        fields = ('displayName','profilePicture')



