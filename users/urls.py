from django.urls import path
from users.views import LoginUserView, LogoutUserView, JoinView, ProfileView

app_name = 'users'

urlpatterns = [
    path('join/', JoinView.as_view(), name='join'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
]
