from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from instagram.forms import PostForm

# Create your views here.
@login_required(login_url='login')
def create_post(request, user_id):
    if request.user.id != user_id:
        return redirect('home')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('profile_detail', pk=user_id)
    else:
        form = PostForm()
    
    return render(request, 'create_post.html', {'form': form})
