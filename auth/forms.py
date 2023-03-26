from django.contrib.auth import forms

from auth.models import BlogUser


class UserCreationForm(forms.UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {
            'class': 'input',
        }
        self.fields['email'].widget.attrs = {
            'class': 'input',
        }
        self.fields['password1'].widget.attrs = {
            'class': 'input',
        }
        self.fields['password2'].widget.attrs = {
            'class': 'input',
        }

    class Meta(forms.UserCreationForm.Meta):
        model = BlogUser
        fields = ('username', 'email')


class UserChangeForm(forms.UserChangeForm):

    class Meta(forms.UserChangeForm.Meta):
        model = BlogUser
        fields = ('username', 'email')
