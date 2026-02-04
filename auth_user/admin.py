from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, Profile


class ProfileInline(admin.StackedInline):
    """Inline Profile in User Admin"""
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class UserAdmin(BaseUserAdmin):
    """Custom User Admin"""
    inlines = (ProfileInline,)
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined']
    list_filter = ['is_staff', 'is_superuser', 'is_active', 'date_joined']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    ordering = ['-date_joined']
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'phone')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )


class ProfileAdmin(admin.ModelAdmin):
    """Profile Admin"""
    list_display = ['user', 'location', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['user__username', 'user__email', 'location', 'skills_offered', 'skills_wanted']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('User', {'fields': ('user',)}),
        ('Profile Info', {'fields': ('bio', 'profile_pic', 'location')}),
        ('Skills', {'fields': ('skills_offered', 'skills_wanted')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )


# Unregister default User admin and register custom one
admin.site.register(CustomUser, UserAdmin)
admin.site.register(Profile, ProfileAdmin)