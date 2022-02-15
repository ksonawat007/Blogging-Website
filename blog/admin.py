from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'headline',
        'tagline',
    ]
    readonly_fields = [
        'published',
        'author',
        'rating',
    ]