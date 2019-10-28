from django.shortcuts import render, get_object_or_404
from .models import Post,Category,Comment
from .forms import CommentForm



def blog_index(request):
    posts       = Post.objects.all().order_by('-created_on')
    context     = {'posts':posts}
    return render(request, 'blog/blog_index.html', context)

def blog_category(request, category):
    posts       = Post.objects.filter(categories__name__contains=category).order_by('-created_on')
    context     = {'posts':posts, 'category':category}

    return render(request, 'blog/blog_category.html', context)

def blog_detail(request, pk):
    post        = get_object_or_404(Post, pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author  = form.cleaned_data['author'],
                body    = form.cleaned_data['body'],
                post    = post
            )
            comment.save()


    comments    = Comment.objects.filter(post=post)
    context     = {'post':post, 'comments':comments, 'form':form}
    return render(request, 'blog/blog_detail.html', context)