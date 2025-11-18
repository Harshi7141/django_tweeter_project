from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    # Meta class banvto mag pudhe jato standard way ahe karavch lagtay.
    class Meta:
        model = Tweet
        # Mag sangaych kiti field use kartoy karan saglya thodi use karnar ahe mhnun. 
        fields = ['text', 'photo']

'''Mag zhala ki views madhe jaych logic sathi.'''

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')