from django.urls import path

from blog.views import AboutView, ContactsView, MainView

app_name = 'blog'

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('about/', AboutView.as_view(), name='about'),
    path('contacts/', ContactsView.as_view(), name='contacts')
]
