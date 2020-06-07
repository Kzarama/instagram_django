from django.views.generic import DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy

from users.forms import SignupForm
from users.models import Profile
from posts.models import Post

# User detail view
class UserDetailView(LoginRequiredMixin, DetailView):
    # Template name
    template_name = 'users/detail.html'
    # Slug field - for identification
    slug_field = 'username'
    # url of the kwarg slug
    slug_url_kwarg = 'username'
    # query of the user at the database
    queryset = User.objects.all()
    # context object name
    context_object_name = 'user'

    # Get_context_data
    def get_context_data(self, **kwargs):
        # Get the context of the view
        context = super().get_context_data(**kwargs)
        # User 
        user = self.get_object()
        # Assign posts to the context of the application
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        # Return context
        return context

# Sign up view
class SignupView(FormView):
    # Template name
    template_name = 'users/signup.html'
    # Form of the sign up
    form_class = SignupForm
    # Success url - when if correct redirect to this 
    success_url = reverse_lazy('users:login')

    # Save the data
    def form_valid(self, form):
        # Save the form
        form.save()
        # Return the form
        return super().form_valid(form)

# Update profile view
class UpdateProfileView(LoginRequiredMixin, UpdateView):
    # Template name
    template_name = 'users/update_profile.html'
    # Profile of the user
    model = Profile
    # Fields of the view
    fields = ['website', 'biography', 'phone_number', 'picture']

    # get object of the view
    def get_object(self):
        # Return the profile
        return self.request.user.profile

    # success url
    def get_success_url(self):
        # Username
        username = self.object.user.username
        # Return the url
        return reverse('users:detail', kwargs={'username': username})

# Login view
class LoginView(auth_views.LoginView):
    # Template name
    template_name = 'users/login.html'

# logout view
class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    # Template name
    template_name = 'users/logged_out.html'