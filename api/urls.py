from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, LikeViewSet, UserViewSet


router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'likes', LikeViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]