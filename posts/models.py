from django.db import models
from django.contrib.auth.models import User

# Model of posts constrains of the fields posts
class Post(models.Model):
    # fk owner user of the post
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # fk profile 
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    # Title of the post
    title = models.CharField(max_length=255)
    # Photo of the post
    photo = models.ImageField(upload_to='posts/photos')
    # Date of creation of the post
    created = models.DateTimeField(auto_now_add=True)
    # Date of modification of the post
    modified = models.DateTimeField(auto_now=True)

    # str method
    def __str__(self):
        return '{} by @{}'.format(self.title, self.user.username)