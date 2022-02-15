from django.contrib import admin
from .models import Author, Post
# Register your models here.
admin.site.register([Author,Post])