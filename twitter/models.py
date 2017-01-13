from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


# Create your models here.


class TwitterUser(AbstractUser):
    mug_shot = models.ImageField(upload_to='/uploads/mugs', null=True, blank=True)

class Twit(models.Model):
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(TwitterUser)