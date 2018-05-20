import datetime

from oscar.core.loading import get_model

from django.views import generic

Post = get_model('appblog', 'Post')
Category = get_model('appblog', 'Category')


class BlogPostView(generic.ListView):

    template_name = 'appblog/blog-post-list.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.get_queryset()
        context['categories'] = self.get_categories()
        return context

    def get_posts_published(self):
        return Post.objects.filter(post_date__lte=datetime.date.today())

    def get_categories(self):
        return Category.objects.all()

    def get_queryset(self):
        queryset = self.get_posts_published()
        queryset = self.apply_search(queryset)
        return queryset

    def apply_search(self, queryset):
        search = self.request.GET.get('search')
        if search is None or search is '':
            return queryset

        queryset = queryset.filter(title__icontains=search)

        return queryset


class BlogPostDetailDetailView(generic.DetailView):

    template_name = 'appblog/blog-post-detail.html'
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = self.get_categories()
        return context

    def get_object(self, queryset=None):
        return Post.objects.get(slug=self.kwargs['slug'])

    def get_categories(self):
        return Category.objects.all()


class BlogCategoryView(generic.ListView):

    template_name = 'appblog/blog-post-list.html'
    model = Post
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = self.get_categories()
        context['posts'] = self.get_posts_published_by_category()
        return context

    def get_categories(self):
        return Category.objects.all()

    def get_posts_published_by_category(self):
        return Post.objects.all().filter(abstractcategorygroup__category__slug=self.kwargs['slug'])
