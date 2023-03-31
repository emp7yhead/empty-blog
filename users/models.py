from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    class Meta(object):
        db_table = 'users'
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.username
