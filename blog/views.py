from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')

def users_view(request):
    return render(request, 'users.html')

def blogs_view(request):
    return render(request, 'blogs.html')

def comments_view(request):
    return render(request, 'comments.html')

def categories_view(request):
    return render(request, 'categories.html')

def blog_details_view(request):
    return render(request, 'blogdetails.html')