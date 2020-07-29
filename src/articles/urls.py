from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet

router = DefaultRouter()
router.register(r'article', ArticleViewSet)
urlpatterns = router.urls
