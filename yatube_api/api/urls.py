from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

COMMENTS_URL_PATTERN = r"posts/(?P<post_id>\d+)/comments"

v1_router = DefaultRouter()
v1_router.register("posts", PostViewSet, basename="posts")
v1_router.register("groups", GroupViewSet, basename="groups")
v1_router.register(COMMENTS_URL_PATTERN, CommentViewSet, basename="comments")

urlpatterns = [
    path("v1/api-token-auth/", obtain_auth_token),
    path("v1/", include(v1_router.urls)),
]
