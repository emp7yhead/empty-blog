from django.contrib.auth import forms

from users.models import User


class CustomUserCreationForm(forms.UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {
                'class': 'input',
            }

    class Meta(forms.UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')
        error_messages = {
            'username': {
                'unique': 'Username must be unique',
            },
        }


class UserChangeForm(forms.UserChangeForm):

    class Meta(forms.UserChangeForm.Meta):
        model = User
        fields = ('username', 'email')


class CustomAuthenticationForm(forms.AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {
                'class': 'input',
            }

    class Meta(forms.UserChangeForm.Meta):
        model = User
        fields = ('username', 'password')
