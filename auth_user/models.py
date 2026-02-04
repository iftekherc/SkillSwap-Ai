from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    """Custom User Model"""
    email = models.EmailField(unique=True, verbose_name='Email Address')
    phone = models.CharField(max_length=15, blank=True, null=True)
    
    USERNAME_FIELD = 'username'  
    REQUIRED_FIELDS = ['email'] 
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Profile(models.Model):
    """User Profile - Auto-created on signup"""
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, blank=True, help_text='Tell us about yourself')
    profile_pic = models.ImageField(
        upload_to='profile_pics/', 
        default='default.jpg',
        blank=True
    )
    location = models.CharField(max_length=100, blank=True)
    skills_offered = models.CharField(max_length=200, blank=True, help_text='Comma separated skills you can teach')
    skills_wanted = models.CharField(max_length=200, blank=True, help_text='Skills you want to learn')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"


# Signal to auto-create profile when user registers
@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()