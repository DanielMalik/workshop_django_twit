from django.contrib import admin
from twitter.models import TwitterUser, Twit, Message

# Register your models here.

@admin.register(TwitterUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'mug_shot', 'password', 'mug')

    def mug(self, obj):
        return "<img src ='/{}' width='150' height='150' >".format(obj.mug_shot)

    mug.allow_tags = True

@admin.register(Twit)
class TwitAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'content')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'reciver', 'date', 'content', 'is_read')