from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path("api/", include(router.urls)),
    # path("", views.index, name="home"),
    # path("article", views.ArticleList.as_view(), name="article"),
    # path("articledetail/<int:id>", views.ArticleDetail.as_view(), name="articledetail"),
]
