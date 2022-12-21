from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SingUpForm(UserCreationForm):
  email = forms.EmailField()
  primer_nombre = forms.CharField(max_length = 100)
  apellido = forms.CharField(max_length = 100)

  class Meta:
    model = User
    fields = ('username', 
              'primer_nombre',
              'apellido', 
              'email')
