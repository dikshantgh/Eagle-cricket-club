from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import ModelFormMixin

from blog.forms import BlogCreateForm, CommentCreateForm
from blog.models import Blog
from cricket.models import Kheladi


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    paginate_by = 3


class BlogDetailView(ModelFormMixin, DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    form_class = CommentCreateForm
    success_message = "Thank You! Your comment is added..."

    def dispatch(self, request, *args, **kwargs):
        self.get_object().set_view()
        return super(BlogDetailView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kheladi_list'] = Kheladi.objects.all()
        context['current_user'] = str(self.request.user).lower()
        context['updating_user'] = str(get_object_or_404(Blog, uuid=self.kwargs['uuid']).author).lower()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            form.instance.commented_by = self.request.user
            form.instance.comment_text = form.cleaned_data['comment_text']
            form.instance.blog = self.get_object()
            form.save()
            messages.success(request, self.success_message)
        return HttpResponseRedirect(self.get_object().get_absolute_url())


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'blog/blog_create.html'
    form_class = BlogCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(BlogCreateView, self).form_valid(form)


class BlogUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Blog
    template_name = 'blog/blog_update.html'
    form_class = BlogCreateForm
    success_message = 'Thank You ! Blog Updated Successfully...'

    def dispatch(self, request, *args, **kwargs):
        current_user = str(self.request.user)
        updating_user = str(get_object_or_404(Blog, uuid=self.kwargs['uuid']).author)
        if current_user.lower() == updating_user.lower():
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


class SearchResultListView(ListView):
    model = Blog
    # context_object_name = 'blog_list'
    template_name = 'blog/search_results.html'
    paginate_by = 3

    def get_queryset(self):  # for search results
        query = self.request.GET.get('q')
        return Blog.objects.filter(Q(title__icontains=query) | Q(author__username__icontains=query))


class BlogByTagListView(ListView):
    model = Blog
    template_name = 'blog/blog_list_tag.html'
    paginate_by = 3

    def get_queryset(self):
        return Blog.objects.filter(tag__slug=self.kwargs['tag_slug'])
