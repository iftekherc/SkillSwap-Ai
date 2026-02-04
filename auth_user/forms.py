from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Profile


class UserRegistrationForm(UserCreationForm):
    """Custom Registration Form with Email"""
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email'
        })
    )
    phone = forms.CharField(
        required=False,
        max_length=15,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Phone number (optional)'
        })
    )
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Choose a username'
            })
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes to password fields
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Create a password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm password'
        })
        self.fields['password1'].help_text = ""
        self.fields['password2'].help_text = ""
    
    def clean_email(self):
        """Check if email already exists"""
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already registered.')
        return email


class LoginForm(forms.Form):
    """Custom Login Form"""
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )


class UserUpdateForm(forms.ModelForm):
    """Form for updating user information"""
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email address'
        })
    )
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone number'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First name (optional)'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last name (optional)'
            })
        }
    
    def clean_email(self):
        """Check if email is already taken by another user"""
        email = self.cleaned_data.get('email')
        user_id = self.instance.id
        
        if CustomUser.objects.filter(email=email).exclude(id=user_id).exists():
            raise forms.ValidationError('This email is already in use.')
        return email


class ProfileUpdateForm(forms.ModelForm):
    """Form for updating user profile"""
    
    class Meta:
        model = Profile
        fields = ['bio', 'profile_pic', 'location', 'skills_offered', 'skills_wanted']
        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Tell us about yourself...'
            }),
            'profile_pic': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your location'
            }),
            'skills_offered': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Python, Guitar, Cooking'
            }),
            'skills_wanted': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Web Design, Spanish, Photography'
            })
        }