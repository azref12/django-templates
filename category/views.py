from django.shortcuts import render

def category (request) :
    context = {
        'category' : 'Category',
        'app_css' : 'category/css/styles1.css',
    }
    
    return render (request, 'category/category.html', context)
