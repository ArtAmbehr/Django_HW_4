"""
Some Infos
"""
from django.contrib import admin
from django.urls import path, include
from myapp import views as views_myapp
from django.conf import settings  # настройка media
from django.conf.urls.static import static  # настройка media

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views_myapp.hello_world),  # Таким образом вывел для себя
    path("myapp/", include('myapp.urls')),
]

# настройка media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
