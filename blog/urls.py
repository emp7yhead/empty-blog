from django.urls import path

from blog.views import AboutView, ContactsView, IndexView

app_name = 'blog'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('contacts/', ContactsView.as_view(), name='contacts')
]
