from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/", views.profile_view, name="profile_detail"),
]
