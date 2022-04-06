from django.shortcuts import redirect, render
from . models import Post
from django.contrib.auth.models import User

# Create your views here.


def home(request):
    posts = Post.objects.all
    users = User.objects.all
    return render(request, 'index.html', {'posts': posts, "users": users})


def post_details(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'post_details.html', {'post': post})


def create_post(request):
    if request.method == "POST":

        title = request.POST['title']
        status = request.POST['status']
        body = request.POST['body']
        cUser = request.user
        #slug = title.replace(" ", "-")
        myPost = Post.objects.create(title=title,
                                     body=body,
                                     author=cUser,
                                     status=status)

        myPost.save()
        return redirect('home')
    return render(request, 'create_post.html', {})
