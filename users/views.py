from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserRegistrationForm

class SignUpView(CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
