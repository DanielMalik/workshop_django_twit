"""workshop_twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from twitter.views import TwitView, TwitCreate, UserTwitListView, TwitDetailsView, MessagesListView, MessageCreate, MessageDetailsView

from django.contrib.auth.views import logout_then_login

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^logout/$', logout_then_login, name='site-logout'),
    url(r'^add_twit', TwitCreate.as_view(), name='add-twit'),
    url(r'^twits/', TwitView.as_view(), name='index'),
    url(r'^user/(?P<user>([a-zA-z0-9\.\-])+)$', UserTwitListView.as_view(), name="users-tweets"),
    url(r'^tweet/(?P<pk>(\d)+)$', TwitDetailsView.as_view(), name="tweet"),
    url(r'^messages/$', MessagesListView.as_view(), name="messages"),
    url(r'^add_message/$', MessageCreate.as_view(), name="message"),
    url(r'^message/(?P<pk>(\d)+)$', MessageDetailsView.as_view(), name="message-details"),

]
