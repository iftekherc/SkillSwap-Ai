from django.urls import path
from .views import (
    RegisterView,
    ProfileView,
    ProfileUpdateView,
    PublicProfileView
)
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView


urlpatterns = [
    # Authentication URLs
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    # Profile URLs
path('profile/', ProfileView.as_view(), name='profile'),
path('profile/update/', ProfileUpdateView.as_view(), name='profile_update'),
path('profile/<str:username>/', PublicProfileView.as_view(), name='public_profile'),

# Password URLs
path('change-password/', PasswordChangeView.as_view(template_name='auth/change_password.html'), name='change_password'),
]