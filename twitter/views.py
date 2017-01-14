from django.shortcuts import render
from twitter.models import Twit, Message, TwitterUser
from django.views.generic import ListView, DetailView, CreateView

from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

# Create your views here.

class TwitCreate(CreateView):
    model = Twit
    fields = ['content']
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TwitCreate, self).form_valid(form)

class TwitView(ListView):
    model = Twit

class UserTwitListView(ListView):
    model = Twit

    def get_queryset(self, **kwargs):
        if 'user' in self.kwargs:
            user = get_object_or_404(TwitterUser, username=self.kwargs['user'])
        else:
            user = self.request.user
        return Twit.objects.filter(user=user)

class TwitDetailsView(DetailView):
    model = Twit


class MessageDetailsView(DetailView):
    model = Message

    def get_object(self, **kwargs):
        obj =  Message.objects.get(pk=self.kwargs['pk'])
        if obj.reciver == self.request.user:
            obj.is_read = True
            obj.save()
        return obj

class MessagesListView(ListView):
    model = Message

    def get_queryset(self, **kwargs):
        return Message.objects.filter(reciver=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(MessagesListView, self).get_context_data(**kwargs)
        context['sender'] = Message.objects.filter(sender=self.request.user)
        return context

class MessageCreate(CreateView):
    model = Message
    fields = ['reciver', 'content']
    success_url = reverse_lazy("messages")

    def form_valid(self, form):
        form.instance.sender = self.request.user
        return super(MessageCreate, self).form_valid(form)