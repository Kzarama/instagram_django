from django.shortcuts import redirect
from django.urls import reverse

# Middleware for constrain the entry at the application without complete a user profile
class ProfileCompletionMiddleware:
    
    # Initialization the middleware
    def __init__(self, get_response):
        # Assign the get_response
        self.get_response = get_response

    # Method to call the middleware
    def __call__(self, request):
        # Ensure that the user is logged
        if not request.user.is_anonymous:
            # Assign the profile of the user
            profile = request.user.profile
            # check that the user is not staff and don't have picture or biography and the 
            if not profile.user.is_staff and (not profile.picture or not profile.biography) and (request.path not in [reverse('users:update'), reverse('users:logout')]):
                # Redirect to update profile
                return redirect('users:update')
        # Assign response of the request if the conditions be false
        response = self.get_response(request)
        # Return the response
        return response