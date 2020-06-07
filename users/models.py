from django.db import models

from django.contrib.auth.models import User
from django.db import models

# Constrains of the profile of the user
class Profile(models.Model):
    # User 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Website field
    website = models.URLField(max_length=200, blank=True)
    # Biography field
    biography = models.TextField(blank=True)
    # Phone number field
    phone_number = models.CharField(max_length=20, blank=True)
    # Picture field
    picture = models.ImageField(upload_to='users/pictures', blank=True, null=True)
    # Date of creation
    created = models.DateTimeField(auto_now_add=True)
    # Date of modification
    modified = models.DateTimeField(auto_now=True)

    # str method
    def __str__(self):
        return self.user.username
    