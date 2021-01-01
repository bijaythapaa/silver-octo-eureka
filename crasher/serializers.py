from rest_framework import serializers
from .models import Post, Issue


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'title', 'body', 'created_at',)
        model = Post


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'post', 'issue', 'description', 'raised_date',)
        model = Issue
