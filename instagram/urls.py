from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf. urls.static import static

from posts import views as posts_views
from users import views as users_views

# Url patterns of the application
urlpatterns = [
    # Url of the admin view
    path('admin/', admin.site.urls),
    # Urls of the posts views
    path('', include(('posts.urls', 'posts'), namespace='posts')),
    # Urls of the users views
    path('users/', include(('users.urls', 'users'), namespace='users')),
# Add the statics url for the files
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)