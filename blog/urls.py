from django.urls import path

from blog.views import AboutView, ContactsView

app_name = 'blog'

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('contacts/', ContactsView.as_view(), name='contacts')
]
