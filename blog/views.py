from django.shortcuts import render
import blog.models


def get_all_posts(request):
    tag_filter = request.GET.get("tag")
    if tag_filter:
        posts = blog.models.BlogPost.objects.all().filter(tag_id_id=tag_filter)
    else:
        posts = blog.models.BlogPost.objects.all()
    return render(request, 'blog/index.html', {'posts':posts})

def get_post(request, post_id):
    post = blog.models.BlogPost.objects.get(id=post_id)
    return render(request, 'blog/post.html', {'post':post})

