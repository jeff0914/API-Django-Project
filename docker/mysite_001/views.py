from django.shortcuts import render
from rest_framework import generics
from .models import Article
from .serializers import ArticleSerializer
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# This view handles both listing all articles and creating a new article.
# It requires the user to be authenticated using JWT.
class ArticleListCreate(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]

# This view handles retrieving, updating, and deleting a specific article.
# It requires the user to be authenticated using JWT.
class ArticleRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]
    
# This view is specifically for listing all articles.
class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

# A simple view to display a welcome message for the Dailyview API.    
def home(request):
    return HttpResponse("Welcome Dailyview API!")
