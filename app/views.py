
from django.shortcuts import redirect, render
from django.contrib.auth.models import User

from main.models import Post
from . models import Profile
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse


def login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST['username']
            pass1 = request.POST['pass1']
            user = authenticate(username=username, password=pass1)

            if user is not None:
                auth_login(request, user)
                # name = user.first_name
                return redirect('home')

            else:
                messages.error(request, "Your credentials are incorrect")
                return redirect('login')
    else:
        return redirect('home')

    return render(request, 'login.html')


def register(request):

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.success(request, "Username is taken")
                return render(request, 'register.html', {'fname': fname,
                                                         'lname': lname,
                                                         'email': email,
                                                         'pass1': pass1, })
            elif User.objects.filter(email=email).exists():
                messages.success(request, "Email is taken")
                return render(request, 'register.html', {'username': username,
                                                         'fname': fname,
                                                         'lname': lname,
                                                         'pass1': pass1, })
            else:
                myuser = User.objects.create_user(username, email, pass1)
                myuser.first_name = fname
                myuser.last_name = lname

                myuser.save()
                messages.success(
                    request, "You have been successfully registered")
                return redirect('login')
        else:
            messages.success(request, "Password not matching")

    return render(request, 'register.html')


def logout(request):
    auth_logout(request)
    messages.success(request, "You Logged Out!")
    return redirect('login')


def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method == "POST":

            fname = request.POST['fname']
            lname = request.POST['lname']
            bio = request.POST['bio']
            cUser = request.user
            user_profile = Profile.objects.get(user_id=cUser.id)
            if fname:
                cUser.first_name = fname
            if lname:
                cUser.last_name = lname
            cUser.save()
            if bio:
                user_profile.bio = bio
                user_profile.save()
            return render(request, 'profile.html', {})
        posts = Post.objects.all
        return render(request, 'profile.html', {'posts': posts})


def user_profile(request, user_id):
    if Profile.objects.filter(user_id=user_id).exists():
        profile = Profile.objects.get(user_id=user_id)
        posts = Post.objects.filter(author=user_id)
        return render(request, 'user_profile.html', {'user': profile, 'posts': posts})
    else:
        return render(request, 'error_page.html')


def deleteProfile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method == "POST":
            cUser = request.user
            cUser.delete()
            return redirect('login')
    return render(request, 'deleteProfile.html')
