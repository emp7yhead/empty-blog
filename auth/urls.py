from django.urls import path
from auth.views import LoginUserView, LogoutUserView, JoinView

app_name = 'auth'

urlpatterns = [
    path('join/', JoinView.as_view(), name='join'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
]
