from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=35)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Issue(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    issue = models.CharField(max_length=35)
    description = models.TextField()
    raised_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.issue.title()

