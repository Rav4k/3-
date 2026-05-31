from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news_app.urls')),          # веб-маршруты
    path('api/', include('news_app.api_urls')),  # API маршруты
]