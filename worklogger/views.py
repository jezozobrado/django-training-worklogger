from django.shortcuts import render
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView, FormView
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


def home(request):
    context = {}
    return render(request, 'home.html', context)
