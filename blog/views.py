from django.shortcuts import render

def blog (request) :
    context = {
        'subjudul' : 'MyPlaylist',
        'app_css' : 'blog/css/styles.css',
    }
    
    return render (request, 'blog/home.html', context)
