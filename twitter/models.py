from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


# Create your models here.


class TwitterUser(AbstractUser):
    mug_shot = models.ImageField(upload_to='static/media', null=True, blank=True)
    name = models.CharField(max_length=128, default="")
    # group = models.ForeignKey(Group)


class Twit(models.Model):
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(TwitterUser)

    def __str__(self):
        return 'Twit by user: %s @ %s : "%s..."' % (self.user, self.date, self.content[:32])

class Message(models.Model):
    sender = models.ForeignKey(TwitterUser)
    reciver = models.ForeignKey(TwitterUser, related_name='reciver')
    content = models.TextField(null=False, blank=False)
    date = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)


