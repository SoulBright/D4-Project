from django.urls import path
from .views import PostList, PostDetail, post_filter, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView


urlpatterns = [
    path("", PostList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    path("search", post_filter),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('create/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
]
