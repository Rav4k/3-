from rest_framework.routers import DefaultRouter
from .viewsets import NewsViewSet, UserViewSet
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'news', NewsViewSet, basename='api-news')
router.register(r'users', UserViewSet, basename='api-users')

urlpatterns = router.urls
urlpatterns += [
    path('token/', obtain_auth_token, name='api-token'),
]
