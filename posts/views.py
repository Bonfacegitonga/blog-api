from django.shortcuts import render
from .permission import IsAuthorOrReadOnly
# Create your views here.
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer



class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset= Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer