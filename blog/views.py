from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from django import forms
from django.forms.utils import ErrorList
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User  
from django.db.models import Q
from .models import Post

# Post List view section
class PostListView(ListView):
    model = Post
    template_name = "blog/home_list.html"
    context_object_name = 'queryset'
    ordering = ["-create_date"]

    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qs = Post.objects.all()
        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter(
                Q(author__username__iexact = query)|
                Q(description__icontains = query)|
                Q(title__icontains=query))
        return qs


# Indivitusual user's post list view section
class UserProfilePostListView(ListView):
    model = Post  
    template_name = "blog/user_post_list.html"
    ordering = ["-create_date"]
    context_object_name = "queryset"

    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        qs = Post.objects.filter(author=user, is_draft=False)
        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter(
                Q(author__username__iexact = query)|
                Q(description__icontains = query)|
                Q(title__icontains=query))
        return qs


# Post detail view section
class PostDetailView(DetailView):
    model = Post 
    template_name = "blog/post_detail.html"
    context_object_name = 'object'


# New Post Create view section
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post  
    template_name = 'blog/post_create.html'
    fields = ["title", "description"]
    
    def form_valid(self,form):
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
            return super(PostCreateView, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(['User must be login to coutinue!'])
            return self.form_invalid(form)


# Post Edit view section
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post  
    template_name = 'blog/post_create.html'
    fields = ["title", "description"]

    # def form_valid(self, form):
    #     if form.instance.author == self.request.user:
    #         return super(PostUpdateView, self).form_valid(form)
    #     else:
    #         form.errors[forms.forms.NON_FIELD_ERRORS]=ErrorList(['You are not instance user:)'])
    #         return self.form_invalid(form)

    # insted of ---->

    # request.user === post.author section
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False




# Delete Post view section
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post  
    template_name = 'blog/delete_confirm.html'
    success_url = "/"

    # request.user === post.author
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



# about section view section
def about(request):
    return render(request, 'blog/about.html')


