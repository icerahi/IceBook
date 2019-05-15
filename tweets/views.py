from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from tweets.forms import TweetModelForm
from .models import Tweet
from .mixins import FormUserNeededMixin,UserOwnerMixin

#create

class TweetCreateView(FormUserNeededMixin,CreateView):
  #  queryset = Tweet.objects.all()
    template_name = "tweets/create_view.html"
    form_class=TweetModelForm
  #  success_url = reverse_lazy('tweet:detail')


#update
class TweetUpdateView(UserOwnerMixin,LoginRequiredMixin,UpdateView):
    queryset = Tweet.objects.all()
    form_class=TweetModelForm
    template_name = 'tweets/update_view.html'
   # success_url=reverse_lazy("tweet:detail")
    login_url = "/admin/login"


#Delete

class TweetDeleteView(DeleteView):
    model = Tweet
    template_name = "tweets/delete_confirm.html"
    success_url = reverse_lazy("tweet:list")#/tweet/list/


#List/Search
# Retrieve

class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()



class TweetListView(ListView):


    def get_queryset(self, *args, **kwargs):

        qs = Tweet.objects.all()
        print(self.request.GET)
        query=self.request.GET.get('q',None)
        if query is not None:
            qs=qs.filter(
                Q(content__icontains=query)|
                Q(user__username__icontains=query))
        return qs

    
    def get_context_data(self, *args, **kwargs):
        context=super(TweetListView, self).get_context_data(*args,**kwargs)

        context['create_form']=TweetModelForm()
        context['create_url']=reverse_lazy('tweet:create')
        return context



