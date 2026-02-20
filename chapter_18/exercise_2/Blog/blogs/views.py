from django.shortcuts import render,get_object_or_404, redirect
from .models import Blog,BlogPost
from .forms import BlogForm,BlogPostForm

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

def new_blog(request):

    if request.method != 'POST':
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
    context = {'form': form}
    return render(request, 'blogs/new_blog.xhtml', context)

def new_blogpost(request,blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method != 'POST':
        form = BlogPostForm()
    else:
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.blog = blog
            post.save()
            return redirect('blogs:blog', blog_id=blog_id)
# Display a blank or invalid form.
    context = {'blog': blog, 'form': form}
    return render(request, 'blogs/new_blogpost.xhtml', context)

def edit_blogpost(request,blogpost_id):
    post = get_object_or_404(BlogPost, id=blogpost_id)
    blog = post.blog
    if request.method != 'POST':
        form = BlogPostForm(instance=post)
    else:
        form = BlogPostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog', blog_id=blog.id)
    context = {'blogpost': post, 'blog': blog, 'form': form}
    return render(request, 'blogs/edit_blogpost.xhtml',context)
