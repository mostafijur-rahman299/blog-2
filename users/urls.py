from django.urls import path

from .views import user_register, request_user_profile, user_profile
from django.contrib.auth.views import LoginView, LogoutView 

app_name = 'users'

urlpatterns = [
    path('register/', user_register, name='user-register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='user-login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='user-logout'),
    path('profile/', request_user_profile, name='user-profile'),
    path('profile/detail/<username>', user_profile, name='indivisitual-profile-detail')
]