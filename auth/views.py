from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin

from auth.forms import UserCreationForm


class JoinView(CreateView):

    form_class = UserCreationForm
    template_name = 'auth/registration.html'
    success_url = reverse_lazy('auth:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registration'
        context['button'] = 'Register'
        return context


class LoginUserView(SuccessMessageMixin, LoginView):
    template_name = 'auth/login.html'
    success_message = "You're logged in"
    redirect_authenticated_user = True
    next_page = 'blog:latest'

    def get_success_url(self):
        """Change redirect url."""
        return reverse_lazy('blog:latest')

    def get_context_data(self, **kwargs):
        """Define the title and button text."""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        context['button'] = 'Login user'
        return context


class LogoutUserView(SuccessMessageMixin, LogoutView):
    next_page = 'index'

    def dispatch(self, request, *args, **kwargs):
        """Log out and show a logout message."""
        messages.add_message(request, messages.INFO, "You're logged out")
        return super().dispatch(request, *args, **kwargs)
