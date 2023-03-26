from django.urls import path

from blog.views import AboutView, ContactsView, LatestView

app_name = 'blog'

urlpatterns = [
    path('', LatestView.as_view(), name='latest'),
    path('about/', AboutView.as_view(), name='about'),
    path('contacts/', ContactsView.as_view(), name='contacts')
]
