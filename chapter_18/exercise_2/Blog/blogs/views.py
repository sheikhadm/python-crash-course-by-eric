from django.shortcuts import render,get_object_or_404
from .models import Blog,BlogPost

# Create your views here.
def index(request):
    posts = BlogPost.objects.order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'blogs/index.xhtml', context)



def blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    posts = blog.blogpost_set.order_by('-date_added')

    context = {'blog': blog, 'posts': posts}
    return render(request, 'blogs/blog.xhtml', context)