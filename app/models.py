from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile (models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    address = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=11, null=True)
    gender = models.CharField(max_length=255, null=True)
    occupation = models.CharField(max_length = 255, null=True)
    genotype = models.CharField(max_length = 255, null=True)
    is_staff = models.BooleanField(default=False)
    medical_practitioner = models.CharField(max_length = 255, null=True)
    type_of_sickness = models.CharField(max_length = 255, null=True)

    
    def __str__(self):
        return self.user.username

""" @receiver(post_save, sender=User)
def create_user_profile(sender, instance, created,   **kwargs):
    if created:
        Profile.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
 """

# Create your models here.
 