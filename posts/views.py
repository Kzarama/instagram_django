from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView

from posts.forms import PostForm

from posts.models import Post

# Posts view 
class PostsFeedView(LoginRequiredMixin, ListView):
    # Template name
    template_name = 'posts/feed.html'
    # Model of the posts
    model = Post
    # Order to show the data
    ordering = ('-created')
    # Paginate of the feed
    paginate_by = 2
    # Context name of the objects
    context_object_name = 'posts'

# Posts detail view
class PostDetailView(LoginRequiredMixin, DetailView):
    # Template name
    template_name = 'posts/detail.html'
    # Query to retrieve the post - django concatenate the query
    queryset = Post.objects.all()
    # Context name of the objects
    context_objext_name = 'post'

# Create posts iew
class CreatePostView(LoginRequiredMixin, CreateView):
    # Template name
    template_name = 'posts/new.html'
    # Form class of create posts
    form_class = PostForm
    # Url to redirect when create post is correct
    success_url = reverse_lazy('posts:feed')
    # Get context data of the Create data
    def get_context_data(self, **kwargs):
        # Bring the context of the class
        context = super().get_context_data(**kwargs)
        # Change the user context
        context['user'] = self.request.user
        # Change the profile context
        context['profile'] = self.request.user.profile
        # Return the context to Create data
        return context