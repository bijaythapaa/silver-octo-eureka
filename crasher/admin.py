from django.contrib import admin
from .models import Post, Issue


class IssueInline(admin.TabularInline):
    model = Issue


class PostAdmin(admin.ModelAdmin):
    inlines = [
        IssueInline,
    ]

admin.site.register(Post, PostAdmin)
admin.site.register(Issue)
