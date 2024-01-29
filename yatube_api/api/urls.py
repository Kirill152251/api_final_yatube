from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, CommentViewSet, FollowViewSet, GroupViewSet


API_VERSION = 'v1/{}'

router_v1 = DefaultRouter()
router_v1.register(
    API_VERSION.format('posts'),
    PostViewSet,
    basename='posts'
)
router_v1.register(
    API_VERSION.format('groups'),
    GroupViewSet,
    basename='groups'
)
router_v1.register(
    API_VERSION.format(r'posts/(?P<post_id>\d+)/comments'),
    CommentViewSet,
    basename='comments'
)
router_v1.register(
    API_VERSION.format('follow'),
    FollowViewSet,
    basename='follows'
)

urlpatterns = [
    path(API_VERSION.format(''), include('djoser.urls.jwt')),
    path('', include(router_v1.urls)),
]
