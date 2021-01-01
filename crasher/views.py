# from rest_framework import generics, permissions
from rest_framework import generics

from .models import Post, Issue
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, IssueSerializer


class PostList(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class IssueList(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer


class IssueDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly)
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

