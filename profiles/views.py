from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from posts.models import Post
from instagram.forms import EditProfile
from profiles.models import Follow, Profile


# Create your views here.
def profile_view(request, pk):
    user_found = get_object_or_404(User, pk=pk)
    user_post = Post.objects.filter(author=user_found).order_by("-created_at")

    is_following = False

    if request.user.is_authenticated and request.user != user_found:
        is_following = Follow.objects.filter(
            follower=request.user, following=user_found
        ).exists()

    context = {
        "user": user_found,
        "posts": user_post,
        "total_posts": user_post.count(),
        "is_following": is_following,
        "followers_count": user_found.followers.count(),
        "following_count": user_found.following.count(),
    }
    return render(request, "profile_detail.html", {"user_detail": context})


@login_required(login_url='login')
def follow_user(request, user_id):
    target_user = get_object_or_404(User, id=user_id)

    if target_user != request.user:
        Follow.objects.get_or_create(follower=request.user, following=target_user)        

    return redirect(request.META.get("HTTP_REFERER", "home"))


@login_required(login_url='login')
def unfollow_user(request, user_id):
    target_user = get_object_or_404(User, id=user_id)

    Follow.objects.filter(follower=request.user, following=target_user).delete()

    return redirect(request.META.get("HTTP_REFERER", "home"))

@login_required(login_url='login')
def edit_profile(request, user_id):
    if request.user.id != user_id:
        return redirect('home')

    profile = get_object_or_404(Profile, user__id=user_id)

    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES, instance=profile)
        
        if form.is_valid():
            profile_form = form.save()

            new_username = form.cleaned_data.get('username')
            user = profile.user
            user.username = new_username
            user.save()
            return redirect('profile_detail', pk=user_id)
    else:
        form = EditProfile(instance=profile)
    
    return render(request, 'edit_profile.html', {'form': form})
