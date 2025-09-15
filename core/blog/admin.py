from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ['author','title','category','status','created_at','published_at']

admin.site.register(Category)