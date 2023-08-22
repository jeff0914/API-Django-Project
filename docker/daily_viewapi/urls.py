"""daily_viewapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from mysite_001 import views
from mysite_001.serializers import ArticleViewSet
from rest_framework.routers import DefaultRouter
from mysite_001.views import ArticleListView


router = DefaultRouter()
router.register(r'articles', ArticleViewSet)

urlpatterns = [
    path('api/token-auth/', obtain_jwt_token),
    path('api/token-refresh/', refresh_jwt_token),
    path('api/token-verify/', verify_jwt_token),
    path('api/', include(router.urls)),
    path('', views.home, name='home'),
    path('api/articles/', ArticleListView.as_view(), name='article-list'),
    path('api/articles/<int:pk>/', views.ArticleRetrieveUpdateDestroy.as_view(), name='article-retrieve-update-destroy'),
    path('admin/', admin.site.urls),
]
