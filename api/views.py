from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import*
from .serializers import *
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = self.get_object()
        user = User.objects.get(id=request.data.get('user_id'))
        liked = request.data.get('liked')
        like, created = Like.objects.get_or_create(user=user, post=post)
        like.liked = liked
        like.save()
        return Response({'detail': 'Success'})

    @action(detail=True, methods=['get'])
    def liked_users(self, request, pk=None):
        post = self.get_object()
        likes = Like.objects.filter(post=post, liked=True)
        serializer = UserSerializer(likes, many=True)
        return Response(serializer.data)

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer