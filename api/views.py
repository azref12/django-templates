from django.shortcuts import render

def index (request) :
    context = {
        'judul' : 'MyPlaylist',
        # 'banner' : 'img/banner.png',
        
    }
    return render (request, 'index.html', context)