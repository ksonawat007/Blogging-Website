from accounts.models import NewUser
from djongo import models
from django.utils import timezone
import random


class Post(models.Model):
    published = models.DateTimeField(default = timezone.now)
    tagline = models.TextField()
    rating = models.DecimalField(decimal_places=2,max_digits=3,default = round(random.random()%5,2))
    author = models.ManyToManyField(NewUser)
    headline = models.CharField(max_length=100)
    content = models.TextField()
    objects = models.DjongoManager()

    def __str__(self):
        return self.headline
