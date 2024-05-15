from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from movies.models import Profile, Log


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance
        )


@receiver(post_save, sender=User)
def log_user_saved(sender, instance, **kwargs):
    Log.objects.create(
        message=f"user {instance.username} is saved"
    )


@receiver(post_save, sender=Profile)
def log_profile_saved(sender, instance, **kwargs):
    Log.objects.create(
        message=f"profile {instance} is saved"
    )
