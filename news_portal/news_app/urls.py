from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home_view, name='home'),
    path('news/<int:pk>/', views.news_detail_view, name='news_detail'),
    path('news/add/', views.news_create_view, name='news_create'),
    path('news/<int:pk>/edit/', views.news_edit_view, name='news_edit'),
    path('news/<int:pk>/delete/', views.news_delete_view, name='news_delete'),
    path('register/', views.register_view, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/delete/', views.profile_delete_view, name='profile_delete'),
]
