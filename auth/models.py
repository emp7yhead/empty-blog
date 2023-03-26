from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class BlogUser(AbstractUser):
    class Meta(object):
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('account_details', args=[self.pk])
