from django.urls import path

from .views import PostList, PostDetail, IssueList, IssueDetail

urlpatterns = [
    path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("", PostList.as_view(), name="post_list"),
    path('issue/<int:pk>/', IssueDetail.as_view(), name="issue_detail"),
    path("issue/", IssueList.as_view(), name="issue_list"),
]