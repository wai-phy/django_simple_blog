from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from theblog.models import Post
from .forms import PostForm, UpdateForm

# def home(request):
#     return render(request,'home.html',{})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'
    
class PostAddView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
    # fields = ('title', 'body')

class PostUpdateView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'update_post.html'

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    