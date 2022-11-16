from django.shortcuts import render
from .forms import BlogForm

def blog (request) :
    blogforms = BlogForm
    
    context = {
        'subjudul' : 'MyPlaylist',
        'app_css' : 'blog/css/styles.css',
        'blog_form' : blogforms
    }
    
    if request.method == 'POST' :
        context['title'] = request.POST['title']
    
    return render (request, 'blog/home.html', context)
