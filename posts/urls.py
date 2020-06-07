from django.urls import path

from posts import views

# Url patterns and paths
urlpatterns = [
    # Path of the feed view
    path(
        route='', 
        view=views.PostsFeedView.as_view(), 
        name='feed'
    ),
    # Path of the create post view
    path(
        route='posts/new/', 
        view=views.CreatePostView.as_view(), 
        name='create'
    ),
    # Path of detail of the post
    path(
        route='posts/<int:pk>/',
        view=views.PostDetailView.as_view(),
        name='detail'
    )

]
