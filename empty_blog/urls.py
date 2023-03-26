from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html"), name='index'),
    path('blog/', include('blog.urls')),
    path('auth/', include('auth.urls')),
    # path('profile', include('profiles.urls')),
    # path('articles/', include('articles.urls')),
]
