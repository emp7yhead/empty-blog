from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        '',
        TemplateView.as_view(template_name="index.html"),
        name='index'
    ),
    path('blog/', include('blog.urls')),
    path('auth/', include('users.urls')),
    path('posts/', include('posts.urls')),
    # path('articles/', include('articles.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
