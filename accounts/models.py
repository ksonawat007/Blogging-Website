from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class NewUser(models.Model): 
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, blank = True)
    birthDate = models.DateField(null=True,blank=True)
    def __str__(self):
        return self.user.username

@receiver(post_save, sender = User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        NewUser.objects.create(user = instance)

@receiver(post_save, sender = User)
def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()
    print('Profile successfully Updated')