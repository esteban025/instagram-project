from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render


# Create your views here.
def profile_view(request, pk):
    user_found = get_object_or_404(User, pk=pk)
    return render(request, "profile_detail.html", {"user_detail": user_found})
