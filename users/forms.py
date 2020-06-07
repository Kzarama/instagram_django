from django import forms

from django.contrib.auth.models import User
from users.models import Profile

# Form and constrains to sign up view
class SignupForm(forms.Form):
    # Username field 
    username = forms.CharField(min_length=4, max_length=50)
    # Password field
    password = forms.CharField(max_length=70, widget=forms.PasswordInput())
    # Password confirmation field
    password_confirmation = forms.CharField(max_length=70, widget=forms.PasswordInput())
    # First name field
    first_name = forms.CharField(min_length=2, max_length=50)
    # Last name field 
    last_name = forms.CharField(min_length=2, max_length=50)
    # email field
    email = forms.CharField(min_length=6, max_length=70, widget=forms.EmailInput)

    # username validation for unique
    def clean_username(self):
        # username of the user
        username = self.cleaned_data['username']
        # Ensure that the username isn't taken
        if User.objects.filter(username=username).exists():
            # If the username is taken throw a exception
            raise forms.ValidationError('Username is already in use.')
        # return the username if is not taken
        return username

    # Verify that the passwords match
    def clean(self):
        # Save the data
        data = super().clean()
        # Passsword of the user
        password = data['password']
        # Password confirmation of the user
        password_confirmation = data['password_confirmation']
        # Confirm that the passwords match
        if password != password_confirmation:
            # Throws exception is not match
            raise forms.ValidationError('Passwords do not match.')
        # Return the data
        return data

    # Save the user
    def save(self):
        # Data of the user
        data = self.cleaned_data
        # Delete the password confirmation of the data
        data.pop('password_confirmation')
        # User
        user = User.objects.create_user(**data)
        # Profile
        profile = Profile(user=user)
        # Save the profile
        profile.save()