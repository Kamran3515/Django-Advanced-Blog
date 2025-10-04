from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Profile

# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("id","email", "is_staff", "is_active","is_superuser")
    list_filter = ("email", "is_staff", "is_active","is_superuser")
    search_fields = ("email",)
    ordering = ("email",)
    fieldsets = (
        ("Authorisation", {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser",)}),
    )
    add_fieldsets = (
        ("Create User", {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "is_superuser"
            )}
        ),
    )

@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display = ['id','user','first_name','last_name','created_at','updated_at']