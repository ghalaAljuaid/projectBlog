from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('users/', views.users_view, name='users'),
    path('blogs/', views.blogs_view, name='blogs'),
    path('comments/', views.comments_view, name='comments'),
    path('categories/', views.categories_view, name='categories'),
    path('blogs/<int:blog_id>/', views.blog_details_view, name='blogdetails'),
    # Other URL patterns
]