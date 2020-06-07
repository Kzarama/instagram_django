from django.urls import path

from users import views
# Paths of the app
urlpatterns = [
    # Path of login view    
    path(
        route='login/', 
        view=views.LoginView.as_view(), 
        name='login'
    ),
    # Path of logout view
    path(
        route='logout/', 
        view=views.LogoutView.as_view(), 
        name='logout'
    ),
    # Path of signup view
    path(
        route='signup/', 
        view=views.SignupView.as_view(), 
        name='signup'
    ),
    # Path of update profile view
    path(
        route='me/profile/', 
        view=views.UpdateProfileView.as_view(), 
        name='update'
    ),
    # Path of user detail view
    path(
        route='<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),

]
