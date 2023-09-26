from django.shortcuts import render


def get_all_posts(request):
    return render(request, 'blog/index.html', {})

def get_post(request):
    return render(request, 'blog/post.html', {})

def feedbacks(request):
    return render(request, 'blog/feedbacks.html', {})
