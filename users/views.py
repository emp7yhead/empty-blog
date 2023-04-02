from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from users.forms import CustomAuthenticationForm, CustomUserCreationForm
from users.models import User


class JoinView(CreateView):

    form_class = CustomUserCreationForm
    template_name = 'auth/registration.html'
    success_url = reverse_lazy('users:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registration'
        context['button'] = 'Register'
        return context


class LoginUserView(SuccessMessageMixin, LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'auth/login.html'
    success_message = "You're logged in"
    redirect_authenticated_user = True
    next_page = 'posts:latest'

    def get_success_url(self):
        """Change redirect url."""
        return reverse_lazy('posts:latest')

    def get_context_data(self, **kwargs):
        """Define the title and button text."""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        context['button'] = 'Login'
        return context


class LogoutUserView(SuccessMessageMixin, LogoutView):
    next_page = 'index'

    def dispatch(self, request, *args, **kwargs):
        """Log out and show a logout message."""
        messages.add_message(request, messages.INFO, "You're logged out")
        return super().dispatch(request, *args, **kwargs)


class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'users/profile.html'
