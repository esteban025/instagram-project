from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def manage_user_profile(sender, instance, created, **kwargs):
    if created:
        # Crea el perfil solo si el usuario es nuevo
        Profile.objects.create(user=instance)
    else:
        # Para usuarios existentes, usamos get_or_create por seguridad
        # y guardamos solo si el perfil ya existe
        if hasattr(instance, "profile"):
            instance.profile.save()
