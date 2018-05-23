import datetime

from oscar.core.loading import get_model, get_class

from django.views import generic
from django.core.exceptions import ObjectDoesNotExist

Post = get_model('appblog', 'Post')
Category = get_model('appblog', 'Category')
CategoryGroup = get_model('appblog', 'CategoryGroup')

SearchPostForm = get_class('appblog.forms', 'SearchPostForm')


class BlogPostView(generic.ListView):

    template_name = 'appblog/blog-post-list.html'
    model = Post
    paginate_by = 2
    context_object_name = 'posts'
    form_class = SearchPostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = self.get_categories()
        context['form'] = self.form_class()
        return context

    def get_posts_published(self, queryset):
        return queryset.filter(post_date__lte=datetime.date.today())

    def get_categories(self):
        return Category.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = self.get_posts_published(queryset)
        queryset = self.apply_search(queryset)
        return queryset

    def apply_search(self, queryset):
        search = self.request.GET.get('search')
        if search is None or search is '':
            return queryset

        queryset = queryset.filter(title__icontains=search)

        return queryset


class BlogPostDetailView(generic.DetailView):

    template_name = 'appblog/blog-post-detail.html'
    model = Post
    context_object_name = 'post'
    form_class = SearchPostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = self.get_categories()
        context['is_staff'] = self.request.user.is_staff
        context['form'] = self.form_class()
        return context

    def get_object(self, queryset=None):
        post = {}
        try:
            post = Post.objects.get(slug=self.kwargs['slug'])
        except ObjectDoesNotExist:
            return {}

        return post

    def get_categories(self):
        return Category.objects.all()


class BlogCategoryView(generic.ListView):

    template_name = 'appblog/blog-post-list.html'
    model = Post
    context_object_name = 'posts'
    form_class = SearchPostForm
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = self.get_categories()
        context['form'] = self.form_class()
        return context

    def get_categories(self):
        return Category.objects.all()

    def get_posts_published_by_category(self, queryset):
        return queryset.filter(
            post_date__lte=datetime.date.today(), abstractcategorygroup__category__slug=self.kwargs['slug'])

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = self.get_posts_published_by_category(queryset)
        return queryset
