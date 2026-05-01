from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import LoginForm, RegisterForm
from posts.models import Post


# Create your views here.
def home(request):
    all_posts = Post.objects.all().order_by("-created_at")

    followed_ids = []

    if request.user.is_authenticated:
        followed_ids = request.user.following.values_list("following_id", flat=True)

    return render(
        request,
        "home.html",
        {
            "posts": all_posts,
            "followed_ids": followed_ids,
        },
    )


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = LoginForm(request)
    return render(request, "login.html", {"form": form})


def register_view(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("login")

    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})
