from django.contrib import admin

from posts.models import Post

# Model of admin posts
class PostAdmin(admin.ModelAdmin):
    # List of the fields that be show in the admin posts
    list_display = ('pk', 'user', 'profile', 'title', 'photo')
    # links that can redirect to the edit post model
    list_display_links = ('pk', 'user')
    # Fields that can be searched in the searchbar
    search_fields = ('user__username', 'title')
    # List of filters of posts
    list_filter = ('created', 'modified', 'user__is_active', 'user__is_staff')
    # Fields of only read
    readonly_fields = ('created', 'modified', 'user')
    # Sets of fields
    fieldsets = (
        # Set 1
        ('Post',{
            # Fields to show
            'fields' : (('title', 'photo'))
        }),
        # Set 2
        ('Metadata', {
            # Fields to show
            'fields':(
                ('user',),
                ('created', 'modified'),
            )
        })
    )