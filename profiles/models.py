from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    profile_picture = models.ImageField(
        "Imagen de perfil", upload_to="profile_pictures/", blank=True, null=True
    )
    biography = models.TextField("biografia", max_length=500, blank=True)
    birth_date = models.DateField("fecha de nacimiento", null=True, blank=True)
    followers = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="following",
        through="Follow",
    )

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return self.user.username

    def get_avatar_data(self):

        if self.profile_picture:
            return {"is_image": True, "url": self.profile_picture.url}

        # Lista de colores estéticos (puedes usar los tuyos)
        colors = [
            "#f44336",
            "#e91e63",
            "#9c27b0",
            "#673ab7",
            "#3f51b5",
            "#2196f3",
            "#009688",
            "#4caf50",
            "#ff9800",
        ]

        # Usamos el ID del usuario para que el color sea "aleatorio" pero siempre el mismo para ese usuario
        color = colors[self.user.id % len(colors)]

        # Obtenemos la inicial del username (o del nombre si lo tienes)
        initial = self.user.username[0].upper()

        return {"is_image": False, "initial": initial, "color": color}


class Follow(models.Model):
    follower = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="following"
    )
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="followers"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Follow"
        verbose_name_plural = "Follows"
        unique_together = ("follower", "following", "created_at")

    def __str__(self):
        return f"{self.follower} follows {self.following}"
