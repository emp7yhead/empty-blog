from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authn.urls')),
    # path('profile', include('profiles.urls')),
    # path('articles/', include('articles.urls')),
]
