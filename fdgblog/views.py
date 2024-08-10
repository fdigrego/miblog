from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    #ordering = ['-id']
    ordering = ['-created']
    
class ArticleView(DetailView):
    model = Post
    template_name = 'article_details.html'
    
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # con la siguiente línea incluimos a todos los campos del formulario
    # fields = '__all__'
    # en el siguiente caso elegimos los campos que queremos mostrar
    # esto tiene que ser compatible con los campos del modelo
    # fields = ('title', 'title_tag', 'content')
    
class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = EditForm
    # forma selectiva, el author no va a ser editable
    # fields = ('title', 'title_tag', 'content')
    
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')