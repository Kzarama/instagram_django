from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from django.contrib.auth.models import User
from users.models import Profile

# Constrain of the user is registered in 
@admin.register(Profile)
# Model of admin user
class ProfileAdmin(admin.ModelAdmin):
    # fields to show in the admin
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    # fields with link to the edit
    list_display_links = ('pk', 'user')
    # editable fields in the admin
    list_editable = ('phone_number', 'website', 'picture')
    # fields to search
    search_fields = ('user__username', 'user__email', 'user__first_name', 'user__last_name', 'phone_number')
    # filters
    list_filter = ('user__is_active', 'user__is_staff', 'created', 'modified')
    # fields groups
    fieldsets = (
        # Set 1
        ('Profile', {
            # Fields to show
            # 'fields': (('user', 'picture'),), # to show in one line
            'fields': ('user', 'picture'), # To show in many lines
        }),
        # Set 2
        ('Extra information', {
            # Fields to show
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            )
        }),
        # Set 3
        ('Metadata', {
            # Fields to show
            'fields': (('created', 'modified'),),
        })
    )
    # Readonly fields
    readonly_fields = ('created', 'modified')

# Constains of the admin
class ProfileInLine(admin.StackedInline):
    # Profile
    model = Profile
    # Constrains of the Profile
    can_delete = False
    # Verbose name
    verbose_name_plural = 'profiles'

# User admin settings
class UserAdmin(BaseUserAdmin):
    # link added
    inlines = (ProfileInLine,)
    # List of the fields to display
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')

# To change the admin view
admin.site.unregister(User)
admin.site.register(User, UserAdmin)