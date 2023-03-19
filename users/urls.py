from django.urls import path
from users.views import MainView

urlpatterns = [
    path('', MainView.as_view(), name='index'),
]
