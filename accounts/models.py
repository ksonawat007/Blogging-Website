from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class NewUser(models.Model): 
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    bio = models.TextField(max_length=500, blank = True)
    birthDate = models.DateField(null=True,blank=True)

@receiver(post_save, sender = User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        NewUser.objects.create(user = instance)

@receiver(post_save, sender = User)
def save_user_profile(sender,instance,**kwargs):
    if created == False:
        instance.profile.save()
        print('Profile successfully Updated')