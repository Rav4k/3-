from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import News
from .serializers import NewsSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('-date_created')
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['author']
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]   # только чтение для всех