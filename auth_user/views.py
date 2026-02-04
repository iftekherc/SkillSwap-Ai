from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm, LoginForm
from .models import CustomUser, Profile


class RegisterView(View):
    """User Registration View"""
    template_name = 'auth/register.html'
    form_class = UserRegistrationForm

    def get(self, request):
        if request.user.is_authenticated:
            messages.info(request, 'You are already logged in!')
            return redirect('dashboard')
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, f'Account created for {username}! Please log in to continue.')
            return redirect('login')

        return render(request, self.template_name, {'form': form})

class ProfileView(LoginRequiredMixin, View):
    """User Profile View - View only"""
    template_name = 'auth/profile.html'
    login_url = 'login'

    def get(self, request):
        """Display user profile"""
        profile = request.user.profile
        context = {
            'user': request.user,
            'profile': profile
        }
        return render(request, self.template_name, context)


class ProfileUpdateView(LoginRequiredMixin, View):
    """Update User Profile"""
    template_name = 'auth/profile_update.html'
    login_url = 'login'

    def get(self, request):
        """Display profile update form"""
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        """Handle profile update submission"""
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile')

        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, self.template_name, context)

class PublicProfileView(View):
    """View other user's public profile"""
    template_name = 'auth/public_profile.html'

    def get(self, request, username):
        """Display public profile of a user"""
        user = get_object_or_404(CustomUser, username=username)
        profile = user.profile

        context = {
            'profile_user': user,
            'profile': profile,
            'is_own_profile': request.user == user
        }
        return render(request, self.template_name, context)