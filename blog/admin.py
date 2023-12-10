from django.contrib import admin
from .models import User, Post, Comment, Category

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('ID', 'username', 'email')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('ID', 'title', 'category', 'date_published')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('ID', 'post', 'user', 'date_posted')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('ID', 'name')

