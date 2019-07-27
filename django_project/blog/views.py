from django.shortcuts import render

posts = [
    {
        'author': 'AkhilM',
        'title': 'Blog Post 1',
        'content' : 'First Post content',
        'date_posted': 'July 26, 2019',
    },
    {
        'author': 'AviM',
        'title': 'Blog Post 2',
        'content' : 'Second Post content',
        'date_posted': 'July 23, 2019',
    },
]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
