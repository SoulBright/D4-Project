from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.shortcuts import render
from django.core.paginator import Paginator

from .filters import PostFilter
from .models import *
from .forms import PostForm


class PostList(ListView):
    model = Post
    template_name = "posts.html"
    context_object_name = "posts"
    queryset = Post.objects.order_by('-dateCreation')
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class PostDetail(DetailView):
    model = Post
    template_name = "post.html"
    context_object_name = "post"


def post_filter(request):
    f = PostFilter(request.GET, queryset=Post.objects.all())
    return render(request, 'filter_t.html', {'filter': f})


class PostDetailView(DetailView):
    template_name = 'NewsPortal/post_detail.html'
    queryset = Post.objects.all


class PostCreateView(CreateView):
    template_name = 'NewsPortal/post_create.html'
    form_class = PostForm


class PostUpdateView(UpdateView):
    template_name = 'NewsPortal/post_create.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(DeleteView):
    template_name = 'NewsPortal/post_delete.html'
    queryset = Post.objects.all()
    success_url = '/posts/'
