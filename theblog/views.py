from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from .models import Category, Post, Comment
from .forms import AddForm, EditForm, CommentForm
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list': cat_menu_list})
  


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.title().replace('-', ' '))
    return render(request, 'categories.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})


class ArticleView(DetailView):
    model = Post
    template_name = 'article.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


class AddPostView(CreateView):
    model = Post
    form_class = AddForm
    template_name = 'add.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddPostView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


class AddCategoryView(CreateView):
    model = Category
    template_name = 'category.html'
    fields = '__all__'
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddCategoryView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context

class AddQuienView(CreateView):
    model = Category
    template_name = 'quien.html'
    fields = '__all__'
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddQuienView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comments.html'
    
    
    def get_success_url(self):
      return reverse_lazy('article', kwargs={'pk': self.kwargs['pk']})
    
    def form_valid(self, form):
      form.instance.post_id = self.kwargs['pk']
      form.instance.name = self.request.user.username
      return super().form_valid(form)


class EditPostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'edit.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')


