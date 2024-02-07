from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('FruityGame.urls')),
    path('admin/', admin.site.urls),
]
