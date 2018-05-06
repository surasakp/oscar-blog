from django.views import generic
from oscar.core.loading import get_model, get_class
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib import messages
# from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _


Post = get_model('web_blog', 'Post')

PostDetailForm = get_class('web_blog.dashboard.forms', 'PostForm')


class BlogPostListView(generic.ListView):
    template_name = 'web_blog/blog-post.html'
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset


class BlogPostDetailUpdateView(generic.UpdateView):
    template_name = 'web_blog/blog-post-detail.html'
    model = Post
    context_object_name = 'post'
    form_class = PostDetailForm

    def get_object(self, queryset=None):
        print(self.kwargs)
        return get_object_or_404(Post, pk=self.kwargs['post_id'])

    def get_success_url(self):
        messages.success(self.request, _('save success'))

        action = self.request.POST.get('action')
        print('get_success_url action : ', action)
        if action == 'continue':
            url = reverse(
                'blog-dashboard:blog-post-detail', kwargs={"post_id": self.object.id})
        else:
            url = reverse('blog-dashboard:blog-post-list')
        return url


class BlogPostDetailCreateView(generic.CreateView):
    template_name = 'web_blog/blog-post-detail.html'
    model = Post
    context_object_name = 'post'
    form_class = PostDetailForm

    def get_success_url(self):
        messages.success(self.request, _('Post created successfully'))

        action = self.request.POST.get('action')
        if action == 'continue':
            return reverse('blog-dashboard:blog-post-detail', kwargs={'post_id': self.object.id})
        else:
            return reverse('blog-dashboard:blog-post-list')
