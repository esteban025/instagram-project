from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/", views.profile_view, name="profile_detail"),
    path("edit_profile/<int:user_id>/", views.edit_profile, name="edit_profile"),
    path("follow/<int:user_id>/", views.follow_user, name="follow"),
    path("unfollow/<int:user_id>/", views.unfollow_user, name="unfollow"),
]
