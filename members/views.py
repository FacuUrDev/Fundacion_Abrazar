from django.views import generic
from .forms import SingUpForm
from django.urls import reverse_lazy


class UserRegisterView(generic.CreateView):
    form_class = SingUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

